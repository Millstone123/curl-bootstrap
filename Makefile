.PHONY: bootstrap test

bootstrap:
	pip3 install -e .
	python3 -m theme_sync.sync

test:
	python3 -m pytest tests -q
