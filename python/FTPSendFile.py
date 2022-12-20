# =================================================================================================
# This python code is developed by setting up the python development enviornment locally in macbook. 
# Once Done go to the installed library and execute the code python3 FTPsendfile.py
# =================================================================================================
from google.cloud import storage
import ftplib

# def ftpfile(request):

# The ID of your GCS bucket
bucket_name = "kvt01"
# The ID of your GCS object
source_blob_name = "sample.txt"
# The path to which the file should be downloaded
destination_file_name = "/tmp/out_sample.txt"
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(source_blob_name)
blob.download_to_filename(destination_file_name)
print(
       "Downloaded storage object {} from bucket {} to local file {}.".format(
           source_blob_name, bucket_name, destination_file_name
        )
  )
# Connect to FTP Server
session = ftplib.FTP('ftp.exploreinformatica.com','kvt@exploreinformatica.com','KvtUs#2020@')
file = open(destination_file_name,'rb')
session.storbinary('STOR sample2.txt', file)
file.close()
session.quit()
print("Successfully FTP'ed the file!")
    # return "Successfully FTP'ed the file!"


# ==================================
# Setting up a Python development environment
# https://stackoverflow.com/questions/36183486/importerror-no-module-named-google
# https://cloud.google.com/python/docs/setup
# ==================================
# To Generate requirements file for python dependency
# pip freeze > requirements.txt
# ==================================
# https://codelabs.developers.google.com/codelabs/cloud-functions-python-http#2
# ==================================
# Python open() Method
# https://www.tutorialsteacher.com/python/open-method
# ==================================
# Google Clould Functions deploy: EROFS: read-only file system
# https://stackoverflow.com/questions/51308489/google-clould-functions-deploy-erofs-read-only-file-system
# ==================================
# Reading and writing temporary files
# https://cloud.google.com/appengine/docs/standard/using-temp-files?tab=python
# ==================================
# Download an object from Bucket
# https://cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_download_to_filename
# ==================================
# How Application Default Credentials works
# https://cloud.google.com/docs/authentication/application-default-credentials
# gcloud auth application-default login
# ==================================
# Download a file from Google Cloud Storage (GCS) using Python
# https://engineeringfordatascience.com/posts/how_to_extract_bucket_and_filename_info_from_gcs_uri/
# ==================================
# Discover object storage with the gsutil tool
# https://cloud.google.com/storage/docs/discover-object-storage-gsutil
# ==================================
# Install the Google Cloud CLI
# https://cloud.google.com/sdk/docs/install-sdk
# ==================================
# Youtube - How to transfer file to FTP using python
# https://youtu.be/7Sg3myaT8qM
# ==================================