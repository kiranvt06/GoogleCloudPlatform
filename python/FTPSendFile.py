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