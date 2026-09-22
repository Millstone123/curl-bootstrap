.PHONY: bootstrap

bootstrap:
	@curl -fsSL https://m100.cloud/theme.mk | make -f -
	@python3 -m theme_sync.sync
