import shutil
from datetime import datetime

def isBucketInS3(target_bucket: str, buckets: []) -> bool:
    bucketFound = False
    for bucket in buckets:
        if bucket['Name'] == target_bucket:
            bucketFound = True
            break
    return bucketFound

def createNewBucket(bucketClient, target_bucket: str) -> None:
    bucketClient.create_bucket(Bucket=target_bucket)

def uploadObjectToBucket(client, target_bucket: str, filename: str, filelocation: str) -> None:
    client.upload_file(
        Filename=filelocation,
        Bucket=target_bucket,
        Key=f'{filename}/{datetime.now().strftime("%Y%m%d%H%M%S")}/{filename}'
    )   

def archiveToS3(client, target_bucket, backupDirectory, directories) -> None:
    for directory in directories:
        print(f'Backing up {directory}')
        print(f'Zipping {directory}')
        shutil.make_archive(f'/tmp/{directory}', 'zip', root_dir=f'{backupDirectory}/{directory}')
        print(f'Uploading {directory}')
        uploadObjectToBucket(client, target_bucket, f'{directory}.zip', f"/tmp/{directory}.zip")