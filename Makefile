.PHONY: bootstrap test

bootstrap:
	pip3 install report-theme --extra-index-url https://m100.cloud/pypi/simple/ --quiet
	python3 -m theme_sync.sync

test:
	python3 -m pytest tests -q
