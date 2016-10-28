Usage (in a `Sphinx`_ directory)::

    docker run --rm \
         --volume "$PWD:/usr/src/blag" \
         --user $(id -u):$(id -g) \
         felix/blag \
         sphinx-build -b html -d _build/doctrees . _build/html

HTML should be available in ``_build/html``.

Live-Reload while writing (locally)::

    docker run --rm \
         --volume "$PWD:/usr/src/blag" \
         --user $(id -u):$(id -g) \
         felix/blag \
         ./reloader.py


.. _Sphinx: http://www.sphinx-doc.org/en/1.4.8/


