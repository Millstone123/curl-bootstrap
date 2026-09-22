.PHONY: bootstrap test

bootstrap:
	python3 -m pip install -q .
	theme-sync

test:
	python3 -m pytest tests -q
