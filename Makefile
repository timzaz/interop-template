.PHONY: default isvirtualenv

default:
	clear
	@echo "Usage:"
	@echo ""
	@echo "    make format          Formats source files."
	@echo "    make init            Initialises the application."
	@echo "    make test            Runs pytest."
	@echo ""
	@echo ""

isvirtualenv:
	@if [ -z "$(VIRTUAL_ENV)" ]; \
		then echo "ERROR: Not in a virtualenv." 1>&2; exit 1; fi

format:
	poetry run isort ./interop_template ./tests
	autoflake \
		--in-place \
		--recursive \
		--remove-all-unused-imports \
		--remove-unused-variables \
		./interop_template ./tests
	poetry run black ./interop_template ./tests

init:
	cp .sample.env.local .env.local
	poetry config experimental.new-installer true --local
	poetry config installer.parallel true --local
	poetry config virtualenvs.create true --local
	poetry config virtualenvs.in-project true --local
	poetry config virtualenvs.path .venv --local
	poetry install
	poetry install

start:
	python interop_template

test: isvirtualenv
	pytest tests