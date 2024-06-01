FROM python:3.10.2-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git

RUN pip install dvc

ARG GIT_USERNAME
ARG GIT_PASSWORD
ARG APP_DATA_FOLDER

CMD [ "/bin/sh", "-c", "export" ]

RUN git config --global core.autocrlf true

RUN git clone https://$GIT_USERNAME:$GIT_PASSWORD@github.com/angmedin/capstone-project.git

RUN pip install --no-cache-dir -r capstone-project/requirements.txt

RUN cd capstone-project && dvc remote add -d myremote gdrive://$APP_DATA_FOLDER -f
RUN cd capstone-project && dvc remote modify myremote gdrive_use_service_account true
RUN cd capstone-project && dvc remote modify myremote gdrive_acknowledge_abuse true