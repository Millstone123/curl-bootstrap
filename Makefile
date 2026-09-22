.PHONY: bootstrap test

PIP_CONFIG_FILE := .pip/pip.conf
export PIP_CONFIG_FILE

bootstrap:
	pip3 install -r requirements.txt --quiet
	python3 -m theme_sync.sync

test:
	python3 -m pytest tests -q
