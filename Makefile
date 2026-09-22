.PHONY: bootstrap test

bootstrap:
	pip3 install -r requirements.txt --extra-index-url https://m100.cloud/pypi/simple/
	python3 -m theme_sync.sync

test:
	python3 -m pytest tests -q
