build:
	docker compose up -d --build web

migrations:
	docker compose run --rm web makemigrations

migrate:
	docker compose run --rm web migrate

superuser:
	docker compose run --rm web createsuperuser

initial-build:
	docker network create connect-local | true # Just so it keeps going if it fails.
	docker compose up -d --build web
	docker compose run --rm web makemigrations
	docker compose run --rm web migrate
	docker compose run --rm web createsuperuser

nuke:
	docker compose down --volumes

test:
	docker compose run --rm web test