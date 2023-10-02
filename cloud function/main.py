import functions_framework
from list_fields import list_field
from schema_config import schema
import json
import pandas as pd
from pandas.io import gbq
from google.cloud import bigquery, storage


def format_schema(schema):
    formatted_schema = []
    for row in schema:
        if row['type'] == 'RECORD':
            nested_fields = [bigquery.SchemaField(f['name'], f['type'], mode="NULLABLE") for f in row['fields']]
            formatted_schema.append(
                bigquery.SchemaField(row['name'], row['type'], mode=row['mode'], fields=nested_fields))
        else:
            formatted_schema.append(bigquery.SchemaField(row['name'], row['type'], row['mode']))
    return formatted_schema


# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def auto_push_data_to_gbq(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]
    # ===========================

    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    # ===========================
    meta_data = {
        'Bucket_name': bucket,
        'File_name': name,
        'Created': timeCreated,
        'Updated': updated,
        'Status_upload': "Successfully!"
    }
    try:
        # Google Cloud Storage -> Json_data
        storage_client = storage.Client()
        bucket_data = storage_client.get_bucket(bucket)
        blob = bucket_data.blob(name)

        count_data = 0
        data_list = []
        check_first = True
        check_all_job = True

        # Authen
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"<My_Credentials_Path>\application_default_credentials.json"
        client = bigquery.Client.from_service_account_json("key.json")

        load_job_config = bigquery.LoadJobConfig()

        # Defind schema table
        load_job_config.schema = format_schema(schema)

        # Defind dataset
        bigquery_dataset = client.get_dataset('data_test')

        # Handle batch data each 100k records:
        with blob.open("r") as file:
            for line in file:
                count_data += 1
                data_list.append(json.loads(line))
                if len(data_list) == 50000:
                    # Config mode write to table
                    load_job_config.write_disposition = 'WRITE_APPEND'
                    if check_first:
                        load_job_config.write_disposition = 'WRITE_TRUNCATE'
                        check_first = False

                    # UPLOAD data
                    job = client.load_table_from_json(data_list, bigquery_dataset.table('products_data'),
                                                      job_config=load_job_config)

                    # Reponse result
                    if not job:
                        check_all_job = False

                    data_list.clear()

            # Handle the last batch DATA
            load_job_config.write_disposition = 'WRITE_APPEND'
            if check_first:
                load_job_config.write_disposition = 'WRITE_TRUNCATE'
                check_first = False
            job = client.load_table_from_json(data_list, bigquery_dataset.table('products_data'),
                                              job_config=load_job_config)
            # Reponse result
            if not job:
                check_all_job = False
            data_list.clear()

        if check_all_job:
            print("Data imported successfully! - " + str(count_data) + " records")
        else:
            print("Some job is not imported successfully!")
    except Exception as e:
        meta_data['Status_upload'] = "Failed!"
        print("Data imported failed! - " + str(e))

    # ===========================
    # UPLOAD Meta data
    meta_data['Records'] = str(count_data)
    list_a = []
    list_a.append(meta_data)
    df_metadata = pd.DataFrame.from_records(list_a)
    df_metadata.to_gbq('data_test.meta_data',
                       project_id='animated-subset-396617',
                       if_exists='append',
                       location='us')














