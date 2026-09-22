.PHONY: bootstrap test

bootstrap:
	PIP_CONFIG_FILE=.config/pip/pip.conf pip3 install -r requirements.txt --quiet
	python3 -m theme_sync.sync

test:
	python3 -m pytest tests -q
