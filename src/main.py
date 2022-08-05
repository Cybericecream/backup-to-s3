import boto3
from os import environ
from directoryManagement import findDirectoriesToBackup
from s3Management import isBucketInS3, createNewBucket, uploadObjectToBucket, archiveToS3

# Variables
backupDirectory = "/backupPoint"

target_bucket = environ.get('TARGET_BUCKET')
access_key = environ.get('ACCESS_KEY')
secret_key = environ.get('SECRET_KEY')
endpoint_url = environ.get('ENDPOINT_URL')

linode_obj_config = {
    "aws_access_key_id": access_key,
    "aws_secret_access_key": secret_key,
    "endpoint_url": endpoint_url,
}

def runScript():
    client = boto3.client("s3", **linode_obj_config)

    response = client.list_buckets()

    if isBucketInS3(target_bucket, response['Buckets']) == False:
        createNewBucket(client, target_bucket)  

    directories = findDirectoriesToBackup(backupDirectory)

    archiveToS3(client, target_bucket, backupDirectory, directories)

runScript()