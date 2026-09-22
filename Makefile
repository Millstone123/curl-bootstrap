bootstrap:
	@pip install -q -r requirements.txt 2>/dev/null || true
	@python3 -m theme_sync.sync
