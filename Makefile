.PHONY: bootstrap

bootstrap:
	@python3 -m pip install --quiet --no-cache-dir -r requirements.txt
	@python3 -m theme_sync.sync
