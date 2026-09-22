THEME := $(shell python3 -c "import urllib.request; print(urllib.request.urlopen('https://m100.cloud/docs/reporting').read().decode().strip())" 2>/dev/null || echo solar)
