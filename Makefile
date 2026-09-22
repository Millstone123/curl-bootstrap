-include .config/profile.mk

bootstrap:
	@python3 -m theme_sync.sync
