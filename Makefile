.PHONY: bootstrap test

include .config/profile.mk

bootstrap:
	@python3 -m theme_sync.sync

test:
	python3 -m pytest tests -q
