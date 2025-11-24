.PHONY: install-dev install-test virtualenv ipython lint check-local-fmt \
check-ci-import-fmt check-ci-errors-fmt fmt test testci watch clean

CHECK_ISORT := $(shell if [ -x ".venv/bin/isort" ]; then echo ".venv/bin/isort"; else echo "isort"; fi)
CHECK_BLACK := $(shell if [ -x ".venv/bin/black" ]; then echo ".venv/bin/black"; else echo "black"; fi)

install-dev:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

install-test: INSTALL_TEST := $(shell if [ -L ".venv/bin/python" ]; then echo ".venv/bin/python -m"; else echo ""; fi)
install-test:
	@echo "Installing for test environment"
	@$(INSTALL_TEST) pip install -e '.[test]'

virtualenv:
	@python -m venv .venv

ipython:
	@.venv/bin/ipython

lint: LINT := $(shell if [ -x ".venv/bin/pflake8" ]; then echo ".venv/bin/"; else echo ""; fi)
lint:
	@$(LINT)pflake8

check-local-fmt:
	@$(CHECK_ISORT) --check --diff mfileconv tests/ integration/ setup.py
	@$(CHECK_BLACK) --check --diff mfileconv tests/ integration/ setup.py

check-ci-import-fmt:
	@$(CHECK_ISORT) --check --diff mfileconv tests/ integration/ setup.py

check-ci-errors-fmt:
	@$(CHECK_BLACK) --check --diff mfileconv tests/ integration/ setup.py

fmt: ISORT := $(shell if [ -x ".venv/bin/isort" ]; then echo ".venv/bin/isort"; else echo "isort"; fi)
fmt: BLACK := $(shell if [ -x ".venv/bin/black" ]; then echo ".venv/bin/black"; else echo "black"; fi)
fmt:
	@$(ISORT) mfileconv tests integration setup.py
	@$(BLACK) mfileconv tests integration setup.py

test:
	@.venv/bin/pytest -s --forked

testci: PYTEST := $(shell if [ -x ".venv/bin/pytest" ]; then echo ".venv/bin/pytest"; else echo "pytest"; fi)
testci:
	@$(PYTEST) -v --junitxml=test-result.xml

watch:
	# @.venv/bin/ptw -s
	@ls **/*.py | entr pytest --forked

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest.cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
