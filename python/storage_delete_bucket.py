import os
import sys
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'kvt10_sa_key.json'

def delete_bucket(bucket_name):
    """Deletes a bucket. The bucket must be empty."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()

    print(f"Bucket {bucket.name} deleted")

 # [END storage_delete_bucket]

if __name__ == "__main__":
    delete_bucket(bucket_name=sys.argv[1])