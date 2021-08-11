begin: migrate start

start:
	@docker-compose up -d

stop:
	@docker-compose stop

status:
	@docker-compose ps

restart: stop start

clean: stop
	@docker-compose rm --force
	@find . -name \*.pyc -delete

migrate:
	@docker-compose exec backend python ./manage.py migrate

makemigrations:
	@docker-compose exec backend python ./manage.py makemigrations

superuser:
	@docker-compose exec backend python ./manage.py createsuperuser

logs:
	@docker-compose logs -f

.PHONY: start stop status restart clean migrate superuser logs
