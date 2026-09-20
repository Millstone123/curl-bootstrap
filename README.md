# curl-bootstrap

Setup for restricted sandboxes:

```sh
curl -L -o curl-bootstrap.tar.gz https://github.com/Millstone123/curl-bootstrap/archive/HEAD.tar.gz
mkdir -p curl-bootstrap
tar -xzf curl-bootstrap.tar.gz -C curl-bootstrap --strip-components=1
rm curl-bootstrap.tar.gz
cd curl-bootstrap
make bootstrap
```

`make bootstrap` loads the shared theme profile and renders the sample report.
It falls back to the default palette when the service is unavailable.
