build:
	poetry install

run:
	.venv/bin/python start.py

build-pip:
	pip3 install -r requirements.txt

run-pip:
	python3 start.py
