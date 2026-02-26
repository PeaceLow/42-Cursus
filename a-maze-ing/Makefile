PYTHON = python3
PIP = pip
SRC = src


install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(SRC)/main.py

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name "*.pyc" -delete