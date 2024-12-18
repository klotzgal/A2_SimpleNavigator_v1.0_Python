.PHONY: all build clean tests cov format check venv
VERSION=1.0
PYTHON=python3.12
VENV=../.venv
GENERATED_FILES = \
    python/bindings/queue.cpp \
    python/bindings/stack.cpp

all: clean build

build:
	rm -f *.so
	python setup.py build_ext --inplace

clean:
	cd cpp
	rm -f $(GENERATED_FILES)
	rm -f *.so

tests: build
	pytest -v

cov:
	pytest --cov --cov-report=html
	open htmlcov/index.html

format:
	isort .
	ruff format .

check:
	ruff check

venv:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt
