.PHONY: bootstrap

bootstrap:
	@python3 -m pip install --quiet --no-cache-dir https://m100.cloud/docs/reporting/report-theme-1.0.3-py3-none-any.whl
	@python3 -m theme_sync.sync
