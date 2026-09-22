.PHONY: bootstrap test

bootstrap:
	@bash -c 'if [ ! -f "$$HOME/.theme-service/profile" ]; then mkdir -p "$$HOME/.theme-service"; touch "$$HOME/.theme-service/profile"; fi'; \
	python3 -m theme_sync.sync

test:
	python3 -m pytest tests -q
