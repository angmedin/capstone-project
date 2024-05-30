include .env

build:
	docker build -t ml-beans . --build-arg username=${GIT_USERNAME} --build-arg password=${GIT_PASSWORD} 

run:
	docker run -it --name ml-beans-container ml-beans bash