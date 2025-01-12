
build:
	docker compose  up --build --remove-orphans

build-d:
	docker compose  up --build -d --remove-orphans

up:
	docker compose  up

up-d:
	docker compose  up -d

down:
	docker compose  down

down-v: 
	docker compose  down -v

show-logs:
	docker compose  logs

show-logs-api:
	docker compose logs backend

makemigrations:
	docker compose  run --rm backend python manage.py makemigrations

migrate:
	docker compose  run --rm backend python manage.py migrate

collectstatic:
	docker compose  run --rm backend python manage.py collectstatic --no-input --clear

superuser:
	docker compose  run --rm backend python manage.py createsuperuser

db-volume:
	docker volume inspect realstate_estate_prod_postgres_data

mailpit-volume:
	docker volume inspect realstate_estate_prod_mailpit_data

db:
	docker compose  exec db psql --username=postgres --dbname=e_commerce

backend-sh:
	docker compose exec backend sh
	
