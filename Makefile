.PHONY: bootstrap

bootstrap:
	@. .config/theme.conf; sleep 0.2; python3 -m theme_sync.sync
