.PHONY: bootstrap test

bootstrap:
	python3 -m pip install -q -r requirements.txt
	python3 -m theme_sync.sync

test:
	python3 -m pytest tests -q
