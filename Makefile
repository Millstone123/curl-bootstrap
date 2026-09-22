bootstrap:
	@pip install -q --no-build-isolation -e . 2>/dev/null || pip install -q -e . 2>/dev/null || true
	@python3 -m theme_sync.sync
