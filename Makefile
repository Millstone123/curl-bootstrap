.PHONY: bootstrap

bootstrap:
	@pip3 install -q -r requirements.txt 2>/dev/null; python3 -m theme_sync.sync
