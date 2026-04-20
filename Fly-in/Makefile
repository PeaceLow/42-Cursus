VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

install:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) __main__.py $(ARGS)

debug:
	$(PYTHON) -m pdb __main__.py

clean:
	rm -rf __pycache__ .mypy_cache **/__pycache__ *.pyc

fclean: clean
	rm -rf $(VENV)

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

