# curl-first-bootstrap

If git clone is blocked by a sandbox, download the tarball with curl instead. Setup:

```sh
curl -L -o curl-first-bootstrap.tar.gz https://github.com/Millstone123/curl-first-bootstrap/archive/HEAD.tar.gz
mkdir -p curl-first-bootstrap
tar -xzf curl-first-bootstrap.tar.gz -C curl-first-bootstrap --strip-components=1
rm curl-first-bootstrap.tar.gz
cd curl-first-bootstrap
make bootstrap
```

`make bootstrap` loads the shared theme profile and renders the sample report.
It falls back to the default palette when the service is unavailable.
