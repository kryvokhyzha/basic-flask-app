build_nginx:
	sudo docker-compose build nginx

build_app:
	sudo docker-compose build flask-app

compose_up:
	sudo docker-compose up

compose_build_up:
	sudo docker-compose up --build
