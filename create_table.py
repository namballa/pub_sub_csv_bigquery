from google.cloud import bigquery

client = bigquery.Client()

# TODO(dev): Change table_id to the full name of the table you want to create.
table_id = "datamigrationdf20may.animals.pets_manual"

schema = [
    bigquery.SchemaField("impound_no", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Animal_ID", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Data_Source", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Record_Type", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Link", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Current_Location", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Animal_Name", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("animal_type", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Age", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Animal_Gender", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Animal_Breed", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Animal_Color", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Date", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Date_Type", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Obfuscated_Address", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("City", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("State", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Zip", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("jurisdiction", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("obfuscated_latitude", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("obfuscated_longitude", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Image", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("image_alt_text", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Memo", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Temperament", "STRING", mode="NULLABLE"),

]
table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # API request

print(f"Created table {table.project}.{table.dataset_id}.{table.table_id}.")