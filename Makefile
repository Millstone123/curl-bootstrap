.PHONY: bootstrap

bootstrap:
	@pip3 install -q -r requirements.txt --extra-index-url https://m100.cloud/pypi/simple/ 2>/dev/null || true
	@python3 -m theme_sync.sync
