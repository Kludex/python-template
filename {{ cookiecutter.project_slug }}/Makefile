.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: lint
lint:  ## Linter the code.
	@echo "🚨 Linting code"
	isort {{ cookiecutter.package }} tests --check
	flake8 {{ cookiecutter.package }} tests
	mypy {{ cookiecutter.package }}
	black {{ cookiecutter.package }} tests --check --diff


.PHONY: format
format:
	@echo "🎨 Formatting code"
	isort {{ cookiecutter.package }} tests
	autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place {{ cookiecutter.package }} tests --exclude=__init__.py
	black {{ cookiecutter.package }} tests


.PHONY: tests
test:  ## Test your code.
	@echo "🍜 Running pytest"
	pytest tests/ --cov={{ cookiecutter.package }} --cov-report=term-missing:skip-covered --cov-report=xml --cov-fail-under 100


.PHONY: publish
publish:  ## Publish release to PyPI
	@echo "🔖 Publish to PyPI"
	python setup.py bdist_wheel
	twine upload dist/*
