default: install test

.PHONY: install
install:
	poetry install

.PHONY: shell
shell:
	poetry shell

.PHONY: test
test:
	poetry run pytest

.PHONY: install_poetry
install_poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

.PHONY: docker
docker:
	docker build -t loan_payment_calculator:latest .
	docker run loan_payment_calculator
