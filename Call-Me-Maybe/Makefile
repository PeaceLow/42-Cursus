install:
	uv add pydantic uv run flake8 uv run mypy regex types-regex
	mkdir -p data/output

run:
	HF_HOME=/tmp/huggingface uv run python -m src

debug:
	HF_HOME=/tmp/huggingface python -m pdb -m src

clean:
	rm -rf __pycache__ .uv run .mypy_cache .uv run flake8_cache src/__pycache__ llm_sdk/__pycache__ data/output data/output/*

fclean: clean
	rm -rf .venv

lint:
	uv run flake8 .
	uv run mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	uv run flake8 .
	uv run mypy . --strict