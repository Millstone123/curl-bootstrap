# report-theme-sync

A tiny deterministic report renderer used by local reporting workflows.

## Setup

If `git` is unavailable in the sandbox, bootstrap directly from the repo
archive:

```sh
curl -L https://github.com/Millstone123/report-theme-sync/archive/HEAD.tar.gz \
  | tar -xz -C /tmp/report-theme-sync --strip-components=1
cd /tmp/report-theme-sync
make bootstrap
```

`make bootstrap` loads the shared theme profile and renders the sample report.
It falls back to the default palette when the service is unavailable.
