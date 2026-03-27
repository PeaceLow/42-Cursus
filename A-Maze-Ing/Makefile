VENV        = venv
PYTHON      = $(VENV)/bin/python
PIP         = $(VENV)/bin/pip
FLAKE8      = $(VENV)/bin/flake8
MYPY        = $(VENV)/bin/mypy

PKG_DIR     = mazegen_forge
DIST_DIR    = $(PKG_DIR)/dist
BUILD_DIR   = $(PKG_DIR)/build
EGG_INFO    = mazegen_forge.egg-info

.PHONY: all install run debug lint lint-strict build clean fclean re

all: run

$(VENV):
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

install: $(VENV)

run: $(VENV)
	$(PYTHON) a_maze_ing.py config.txt

debug: $(VENV)
	$(PYTHON) -m pdb a_maze_ing.py config.txt

lint: $(VENV)
	$(FLAKE8) .
	$(MYPY) a_maze_ing.py utils/ core/ display/ controllers/ \
		--warn-return-any --warn-unused-ignores \
		--ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict: $(VENV)
	$(FLAKE8) .
	$(MYPY) a_maze_ing.py utils/ core/ display/ controllers/ --strict

build: $(VENV)
	$(PIP) install --quiet build
	cd $(PKG_DIR) && $(CURDIR)/$(PYTHON) -m build
	@echo "Wheel disponible dans $(DIST_DIR)/"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "maze.txt" -delete
	rm -rf $(DIST_DIR) $(BUILD_DIR)

fclean: clean
	rm -rf $(VENV)

re: fclean all
