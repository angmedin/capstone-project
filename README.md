# Capstone Project

## Introduction

This report aims to put into practice the knowledge acquired during the course of the MLOps bootcamp, through a small but enriching exercise that emulates the deployment of an ML pipeline in a professional environment. First, a dataset (Dry Bean Dataset) will be analyzed through an Exploratory Data Analysis. Subsequently, we will explore the challenges and questions that can be addressed and solved by leveraging ML models. Python will act as the main technological conduit to perform our analysis and execution tasks.

> [!NOTE]
>***You will find a more detailed report in PDF format about the analysis and results of this exercise under the doc directory.***
>***You can also find the EDA in the Jupyter Notebook located under doc/eda.***

## Running the project

Add a `.env` file in the root folder containing:

GIT_USERNAME=<your_user>
GIT_PASSWORD='<your_password>'
DATABASE_HOST=<host>
DATABASE_USER=<dry_bean_user>
MYSQL_ROOT_PASSWORD=<password>
MYSQL_DATABASE=<dry_bean>
MYSQL_USER=<dry_bean_user>
MYSQL_PASSWORD=<dry_bean_user_password>
APP_DATA_FOLDER=<folderId>
GDRIVE_CREDENTIALS_DATA=<JSON string with credentials>

Those credentials will be used to run the pipeline and track the metadata and changed files.

Then, execute:

`make build`

`make run`

A bash console is shown and the pipeline can be executed with `dvc exp run`.
