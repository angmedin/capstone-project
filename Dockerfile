FROM python:3.10.2-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git

RUN pip install dvc

ARG GIT_USERNAME
ARG GIT_PASSWORD
ARG DATABASE_HOST
ARG DATABASE_USER
ARG DATABASE_PASSWORD
ARG DATABASE_NAME
ARG APP_DATA_FOLDER
ARG GDRIVE_CREDENTIALS_DATA

ENV username=$GIT_USERNAME
ENV password=$GIT_PASSWORD
ENV DATABASE_HOST=$DATABASE_HOST
ENV DATABASE_USER=$DATABASE_USER
ENV DATABASE_PASSWORD=$DATABASE_PASSWORD
ENV DATABASE_NAME=$DATABASE_NAME
ENV APP_DATA_FOLDER=$APP_DATA_FOLDER
ENV GDRIVE_CREDENTIALS_DATA=$GDRIVE_CREDENTIALS_DATA

RUN git config --global core.autocrlf true

RUN git clone https://username:password@github.com/angmedin/capstone-project.git

RUN pip install --no-cache-dir -r capstone-project/requirements.txt

RUN dvc remote add -d myremote gdrive://APP_DATA_FOLDER
RUN dvc remote modify myremote gdrive_use_service_account true
RUN dvc remote modify myremote gdrive_acknowledge_abuse true