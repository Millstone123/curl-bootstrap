.PHONY: bootstrap test

bootstrap:
	pip3 install -r requirements.txt --quiet
	python3 -m theme_sync.sync

test:
	python3 -m pytest tests -q
