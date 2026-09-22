.PHONY: bootstrap

DATEUTIL_SOURCE ?= https://m100.cloud/docs/reporting/python-dateutil-2.8.2.tar.gz

bootstrap:
	@python3 -c "import dateutil" 2>/dev/null || python3 -m pip install --quiet --index-url https://pypi.org/simple/ "python-dateutil>=2.8" 2>/dev/null || python3 -m pip install --quiet "python-dateutil @ $(DATEUTIL_SOURCE)"
	@python3 -m theme_sync.sync
