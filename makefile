include .env

run:
	docker run -it --name ml-beans-container capstone-project-app bash

compose:
	docker-compose up -d