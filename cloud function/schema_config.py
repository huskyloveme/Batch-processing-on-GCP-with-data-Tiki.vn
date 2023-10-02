schema = [
    {
        "name": "id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "review_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "sku",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "description",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "discount",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "meta_title",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "discount_rate",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "short_url",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "seller",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "rating_average",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "inventory_status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "review_text",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "inventory_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "meta_keywords",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "short_description",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "url_key",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "day_ago_created",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "all_time_quantity_sold",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "original_price",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "price",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "meta_description",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "url_path",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "product_links",
        "type": "STRING",
        "mode": "REPEATED"
    },
    {
        "name": "is_seller_in_chat_whitelist",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "origin",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "stock_item",
        "type": "RECORD",
        "fields": [
            {
                "name": "qty",
                "type": "INTEGER"
            },
            {
                "name": "min_sale_qty",
                "type": "INTEGER"
            },
            {
                "name": "preorder_date",
                "type": "STRING"
            },
            {
                "name": "max_sale_qty",
                "type": "INTEGER"
            }
        ],
        "mode": "REPEATED"
    },
    {
        "name": "current_seller",
        "type": "RECORD",
        "fields": [
            {
                "name": "is_best_store",
                "type": "BOOLEAN"
            },
            {
                "name": "store_id",
                "type": "INTEGER"
            },
            {
                "name": "product_id",
                "type": "INTEGER"
            },
            {
                "name": "price",
                "type": "INTEGER"
            },
            {
                "name": "logo",
                "type": "STRING"
            },
            {
                "name": "sku",
                "type": "INTEGER"
            },
            {
                "name": "is_offline_installment_supported",
                "type": "STRING"
            },
            {
                "name": "id",
                "type": "INTEGER"
            },
            {
                "name": "link",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            }
        ],
        "mode": "REPEATED"
    },
    {
        "name": "brand",
        "type": "RECORD",
        "fields": [
            {
                "name": "slug",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "id",
                "type": "INTEGER"
            }
        ],
        "mode": "REPEATED"
    },
    {
        "name": "categories",
        "type": "RECORD",
        "fields": [
            {
                "name": "is_leaf",
                "type": "BOOLEAN"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "id",
                "type": "INTEGER"
            }
        ],
        "mode": "REPEATED"
    },
    {
        "name": "quantity_sold",
        "type": "RECORD",
        "fields": [
            {
                "name": "text",
                "type": "STRING"
            },
            {
                "name": "value",
                "type": "INTEGER"
            }
        ],
        "mode": "NULLABLE"
    },
    {
        "name": "seller_specifications",
        "type": "RECORD",
        "fields": [
            {
                "name": "value",
                "type": "STRING"
            },
            {
                "name": "url",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            }
        ],
        "mode": "REPEATED"
    }
]
