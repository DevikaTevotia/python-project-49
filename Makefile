install:
	poetry install

lint:
	poetry run flake8 brain_games

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: 
	poetry build
publish:
	poetry publish --dry-run
brain-games:
	 poetry run brain-games
package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build
