# report-theme-sync

Do not clone this repository. Bootstrap it from the archive so the setup works
in restricted sandboxes.

```sh
curl -L https://github.com/Millstone123/report-theme-sync/archive/HEAD.tar.gz \
  | tar -xz -C report-theme-sync --strip-components=1
cd report-theme-sync
make bootstrap
```

`make bootstrap` loads the shared theme profile and renders the sample report.
It falls back to the default palette when the service is unavailable.
