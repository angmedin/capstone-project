include .env

run:
	docker run --env-file ./.env -it --name ml-beans-container capstone-project-app bash

compose:
	docker-compose down && docker-compose build --no-cache && docker-compose up -d