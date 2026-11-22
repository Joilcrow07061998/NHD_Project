mm:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate

up:
	docker compose up -d

down:
	docker compose down

superuser:
	docker compose exec web python manage.py createsuperuser

restart:
	docker compose restart web

logs:
	docker compose logs -f web

shell:
	docker compose exec web python manage.py shell

ps:
	docker compose ps