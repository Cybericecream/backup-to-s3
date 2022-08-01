# Backup to S3
This so far is a very simple python based script to backup a files in a directory to a s3 bucket.

## How to use
Firstly you will need to prep the env variables. Run the following command.
```bash
cp .env.template .env
```
Then add the all the necessary variables. If you add a `target_variable` that doesn't yet exist the script will create the bucket for you.

Once you have prepped the env variables you will only need to add your backup file point under volumes in `docker-compose.yml`.

After you have completed the above your ready to run the script. <br />
The script will walk through all the files in the set directory and upload them to you s3 bucket with versioning under the date.

Run the following to use the script:
```bash
docker-compose up --build
```