.PHONY: bootstrap

bootstrap:
	@make -C service check 2>/dev/null || true
	@python3 -m theme_sync.sync
