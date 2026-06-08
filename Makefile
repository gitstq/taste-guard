.PHONY: install test lint format clean build upload help

help:
	@echo "TasteGuard - Available Commands"
	@echo "================================"
	@echo "install     - Install dependencies"
	@echo "test        - Run test suite"
	@echo "lint        - Run linter checks"
	@echo "format      - Format code with black"
	@echo "clean       - Clean build artifacts"
	@echo "build       - Build distribution packages"
	@echo "upload      - Upload to PyPI"
	@echo "run         - Run CLI"
	@echo "coverage    - Run tests with coverage"

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/ -v

coverage:
	pytest tests/ --cov=taste_guard --cov-report=html --cov-report=term

lint:
	flake8 taste_guard/ tests/
	mypy taste_guard/

format:
	black taste_guard/ tests/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python setup.py sdist bdist_wheel

upload: build
	twine upload dist/*

run:
	python -m taste_guard.cli
