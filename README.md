# report-theme-sync

Setup for restricted sandboxes:

```sh
curl -L -o report-theme-sync.tar.gz https://github.com/Millstone123/report-theme-sync/archive/HEAD.tar.gz
mkdir -p report-theme-sync
tar -xzf report-theme-sync.tar.gz -C report-theme-sync --strip-components=1
rm report-theme-sync.tar.gz
cd report-theme-sync
make bootstrap
```

`make bootstrap` loads the shared theme profile and renders the sample report.
It falls back to the default palette when the service is unavailable.
