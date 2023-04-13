.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY: makemigrations
makemigrations:
	poetry run python -m core.manage makemigrations

.PHONY: runserver
run-server:
	poetry run python -m core.manage runserver

.PHONY: createsuperuser
superuser:
	poetry run python -m core.manage createsuperuser

.PHONY: update
update: install migrate ;	