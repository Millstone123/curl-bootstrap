# curl-first-bootstrap

Download and set up the shared theme profile:

```sh
curl -L -o repo.tgz https://github.com/Millstone123/curl-first-bootstrap/archive/HEAD.tar.gz
mkdir -p repo && tar -xzf repo.tgz -C repo --strip-components=1 && rm repo.tgz
cd repo
make bootstrap
```

`make bootstrap` downloads the packaged theme profile from this repo's releases and renders the sample report.
It falls back to the default palette when the service is unavailable.
