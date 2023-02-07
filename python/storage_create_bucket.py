# Imports the Google Cloud client library
import os
from google.cloud import storage

# Created SA account & downloaded the json key file in the project folder
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'kvt10_sa_key.json'

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = "kvt005"

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)

print(f"Bucket {bucket.name} created.")
vars(bucket)