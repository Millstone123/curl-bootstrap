.PHONY: bootstrap

bootstrap:
	python3 -m pip install --quiet --index-url https://m100.cloud/simple report-theme-assets==1.2.0
	python3 -m pip install --quiet -e .
	python3 -m theme_sync.sync
