import pymongo
import pandas as pd
import subprocess
from list_atri import list_field
from schema_data import schema
import json
import os
from datetime import datetime

# path file
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'output_final_test.jsonl')

user = os.environ.get('user_mongo')
pw = os.environ.get('pw_mongo')

# Seting config
# ========================================================================
url_mongo_sv = f"mongodb://{user}:{pw}@localhost:27017/?authMechanism=DEFAULT"
client = pymongo.MongoClient(url_mongo_sv)
db = client['data_tiki']
collection = db['products']

# Handle data mongo -> file Jsonline
# ========================================================================
with open(file_path, 'w') as file:
    file.write('')

tmp = 0
count_mor = 0

while True:
    result = collection.find({}).skip(tmp).limit(10000)
    stop_w = 0
    for k, i in enumerate(list(result)):
        count_mor += 1
        stop_w += k
        print(count_mor)
        copy_dict = i.copy()
        with open(file_path, 'a') as file:
            for key, value in copy_dict.items():
                if key == 'specifications':
                    origin = "None"
                    for j in value:
                        if j.get('name') == 'Content':
                            for x in j['attributes']:
                                if x.get('code') == 'origin':
                                    origin = x.get('value')
                    i["origin"] = origin
                if key not in list_field:
                    del i[key]

            json_line = json.dumps(i, default=str)
            file.write(json_line + '\n')
    #     if count_mor == 10101:
    #         break
    # if count_mor == 10101:
    #     break
    if stop_w == 0:
        break
    tmp += 10000

client.close()



# Push data to GCS
# ========================================================================
command = "/snap/bin/gsutil cp " + file_path + " gs://upload_file_mark"

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path_log = os.path.join(current_directory, 'log.txt')

try:
    subprocess.run(command, shell=True, check=True)
    with open(file_path_log, 'a') as file:
        file.write("Lệnh đã được thực thi thành công. - ")
        file.write(str(datetime.now().strftime('%A, %d %B %Y %H:%M:%S')) + "\n")
except Exception as e:
    with open(file_path_log, 'a') as file:
        file.write("Lệnh thất bại với mã lỗi: + " + str(e) + " - ")
        file.write(str(datetime.now().strftime('%A, %d %B %Y %H:%M:%S')) + "\n")
