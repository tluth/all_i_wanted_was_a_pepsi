# Makefile for image_processing project

.PHONY: help venv install lint format test clean

help:
	@echo "Available targets:"
	@echo "  venv     - Create a virtual environment using uv"
	@echo "  install  - Install dependencies using uv"
	@echo "  lint     - Run Ruff linter"
	@echo "  format   - Run Ruff formatter (fix style issues)"
	@echo "  test     - Run tests with pytest"
	@echo "  clean    - Remove Python cache and build artifacts"

venv:
	uv venv

install:
	uv pip install

lint:
	ruff check src/ tests/

format:
	ruff format src/ tests/

test:
	pytest

clean:
	rm -rf .venv __pycache__ .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name '__pycache__' -exec rm -rf {} +
