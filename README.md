Usage (in a [Sphinx](https://www.sphinx-doc.org/) directory):
```
docker run --rm \
     --volume "$PWD:/usr/src/blag" \
     --user $(id -u):$(id -g) \
     registry.gitlab.com/felixhummel/blag-build:master \
     sphinx-build -b html -d _build/doctrees . _build/html
```

HTML should be available in `_build/html`.

Live-Reload while writing (locally):
```
docker run --rm \
     --volume "$PWD:/usr/src/blag" \
     --user $(id -u):$(id -g) \
     registry.gitlab.com/felixhummel/blag-build:master \
     ./reloader.py
```
