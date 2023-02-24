# BQ Command to Export BQ table data to a text file

# bq extract --location=US \
# --destination_format CSV \
# --field_delimiter | \
# --print_header=true \
# white-artwork-372200:ds_kvt.Tkvt \
# gs://kvt01/filename.csv


from google.cloud import bigquery
client = bigquery.Client()
bucket_name = 'kvt'
project = "white-artwork-372200"
dataset_id = "lcef_logs"
table_id = "cloudaudit_googleapis_com_data_access_20230215"

destination_uri = "gs://{}/{}".format(bucket_name, "shakespeare.csv")
dataset_ref = bigquery.DatasetReference(project, dataset_id)
table_ref = dataset_ref.table(table_id)

extract_job = client.extract_table(
    table_ref,
    destination_uri,
    # Location must match that of the source table.
    location="US",
)  # API request
extract_job.result()  # Waits for job to complete.

print(
    "Exported {}:{}.{} to {}".format(project, dataset_id, table_id, destination_uri)
)