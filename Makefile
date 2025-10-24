test:
	python -m pytest --cov --cov-report=json:coverage --ctrf report.json -vv  --gherkin-terminal-reporter

build:
	python -m build

clean:
	rm -rf coverage report.json dist/ Manager/manager.egg-info

change:
	pip install git-changelog
	git-changelog > CHANGELOG.md

dev:
	flask --app ./Manager run

routes:
	flask --app ./Manager routes