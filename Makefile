.PHONY: bootstrap

bootstrap:
	@python3 -m theme_sync.sync
	@python3 -m pytest tests/ -q
