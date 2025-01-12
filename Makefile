
build:
	sudo docker compose  up --build --remove-orphans

build-d:
	sudo docker compose  up --build -d --remove-orphans

up:
	sudo docker compose  up

up-d:
	sudo docker compose  up -d

down:
	sudo docker compose  down

down-v: 
	sudo docker compose  down -v

show-logs:
	sudo docker compose  logs

show-logs-api:
	sudo docker compose logs backend

makemigrations:
	sudo docker compose  run --rm backend python manage.py makemigrations

migrate:
	sudo docker compose  run --rm backend python manage.py migrate

collectstatic:
	sudo docker compose  run --rm backend python manage.py collectstatic --no-input --clear

superuser:
	sudo docker compose  run --rm backend python manage.py createsuperuser

db-volume:
	sudo docker volume inspect realstate_estate_prod_postgres_data

mailpit-volume:
	sudo docker volume inspect realstate_estate_prod_mailpit_data

db:
	sudo docker compose  exec db psql --username=postgres --dbname=e_commerce

backend-sh:
	sudo docker compose exec backend sh
	
