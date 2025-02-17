PROJECT_NAME	= to-do-list
PROJECT_VERSION	= $(shell poetry version -s)
PACKAGE_NAME	= to_do_list

lint:
	poetry run ruff check --fix .

fmt:
	poetry run ruff format .

spec:
	poetry run ${PACKAGE_NAME_NAME} spec

start app:
	poetry run uvicorn main:app --reload


down:
	docker compose down

build:
	docker compose build

up:
	docker compose up

run: down fmt build up