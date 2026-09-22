bootstrap:
	@pip install -q -e .
	@python3 -m theme_sync.sync
