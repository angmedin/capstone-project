FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git

RUN pip install dvc

ARG username
ARG password

ENV username=$username
ENV password=$password

RUN git config --global core.autocrlf true

RUN git clone https://username:password@github.com/angmedin/capstone-project.git

RUN pip install --no-cache-dir -r capstone-project/requirements.txt