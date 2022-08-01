FROM python:3.7.13-alpine3.16

WORKDIR /app

COPY ./src .
RUN mkdir backupPoint

RUN pip3 install boto3

CMD [ "python3", "backupScript.py"]