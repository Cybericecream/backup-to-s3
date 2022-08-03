FROM python:3.7.13-alpine3.16 AS install

WORKDIR /app

RUN mkdir backupPoint

RUN pip3 install boto3

FROM install

COPY ./src .

CMD [ "python3", "backupScript.py"]