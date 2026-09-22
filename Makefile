bootstrap:
	@pip install -q -r requirements.txt
	@python3 -m theme_sync.sync
