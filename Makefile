.PHONY: bootstrap test

bootstrap:
	@./scripts/init-profile || true
	@python3 -m theme_sync.sync

test:
	python3 -m pytest tests -q
