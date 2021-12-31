REQUIREMENTS_DEV="requirements-dev.txt"
REQUIREMENTS="requirements.txt"
PACKAGE_NAME="import_monster"

all: install black isort flake8 test clean

black:
	@black ${PACKAGE_NAME}

isort:
	@isort ${PACKAGE_NAME}

flake8:
	@flake8 ${PACKAGE_NAME}

clean:
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -f `find . -type f -name '@*' `
	@rm -f `find . -type f -name '#*#' `
	@rm -f `find . -type f -name '*.orig' `
	@rm -f `find . -type f -name '*.rej' `
	@rm -rf `find . -type d -name '.pytest_cache' `
	@rm -f .coverage
	@rm -rf htmlcov
	@rm -rf build
	@rm -rf cover
	@rm -rf .tox
	@rm -f .develop
	@rm -f .flake

uninstall:
	@pip uninstall ${PACKAGE_NAME} -y

install: uninstall
	@pip install -r ${REQUIREMENTS}
	@echo "Done"

install-dev: uninstall
	@pip install -r ${REQUIREMENTS_DEV}
	@pip install -e .

install-all: install install-dev install-pre-commit

install-pre-commit:
	@pre-commit install

run-pre-commit:
	@pre-commit run --all-files

test:
	@py.test tests

.PHONY: all black isort flake8 install install-dev install-all uninstall clean test
