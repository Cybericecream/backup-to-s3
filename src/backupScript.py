import boto3
from os import walk, environ
from datetime import datetime

# Variables
backupDirectory = "./backupPoint"

target_bucket = environ.get('TARGET_BUCKET')
access_key = environ.get('ACCESS_KEY')
secret_key = environ.get('SECRET_KEY')
endpoint_url = environ.get('ENDPOINT_URL')

linode_obj_config = {
    "aws_access_key_id": access_key,
    "aws_secret_access_key": secret_key,
    "endpoint_url": endpoint_url,
}

def findFilesToBackup(backupDirectory: str) -> []:
    files = []
    for (dirpath, dirnames, filenames) in walk(backupDirectory):
        files.extend(filenames)
        break
    return files

def isBucketInS3(target_bucket: str, buckets: []) -> bool:
    bucketFound = False
    for bucket in buckets:
        if bucket['Name'] == target_bucket:
            bucketFound = True
            break
    return bucketFound

def createNewBucket(bucketClient, target_bucket: str) -> None:
    bucketClient.create_bucket(Bucket=target_bucket)

def uploadObjectToBucket(target_bucket: str, filename: str, filelocation: str) -> None:
    client.upload_file(
        Filename=filelocation,
        Bucket=target_bucket,
        Key='{}/{}/{}'.format(filename, datetime.now().strftime("%Y%m%d%H%M%S"), filename)
    )   

client = boto3.client("s3", **linode_obj_config)

response = client.list_buckets()

if isBucketInS3(target_bucket, response['Buckets']) == False:
    createNewBucket(client, target_bucket)  

files = findFilesToBackup(backupDirectory)

for file in files:
    uploadObjectToBucket(target_bucket, file, "{}/{}".format(backupDirectory, file))