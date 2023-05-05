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

.PHONY: superuser
superuser:
	poetry run python -m core.manage createsuperuser

.PHONY: test
test:
	poetry run python -m core.manage test


.PHONY: collectstatic
collectstatic:
	poetry run python -m core.manage collectstatic --noinput

.PHONY: update
update: install migrate ;	

.PHONY: lint
lint:
	poetry run pylint --load-plugins pylint_django --fail-under=9 --django-settings-module=TEDx.settings --rcfile=.pylintrc **/*.py

.PHONY: requirements
requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes