.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: lint
lint:  ## Linter the code.
	isort {{ cookiecutter.package }} --check
	flake8 .
	mypy .

.PHONY: test
test:  ## Test your code.
	poetry run pytest tests/ --cov={{ cookiecutter.package }} --cov-report=term-missing:skip-covered --cov-report=xml
