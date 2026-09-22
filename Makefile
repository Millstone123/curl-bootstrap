.PHONY: bootstrap test

bootstrap:
	PIP_EXTRA_INDEX_URL=https://m100.cloud/pypi/simple/ python3 -m pip install -q -r requirements.txt
	python3 -m theme_sync.sync

test:
	python3 -m pytest tests -q
