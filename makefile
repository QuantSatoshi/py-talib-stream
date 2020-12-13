test:
	pytest

install:
	pip install -e .

format:
	isort .
	black .

dev-install:
	pip install black==20.8b1
	pip install isort==5.6.4
