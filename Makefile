.PHONY: bootstrap

bootstrap:
	python3 -m pip install --quiet -r requirements.txt
	python3 -m pip install --quiet -e .
	python3 -m theme_sync.sync
