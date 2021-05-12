cd "$(dirname "$0")"
rm -rf _build
rm -rf source
sphinx-apidoc -M -f -t ./templates -o source ../pyltx ../dist* ../build* ../pyltx.egg* ../pyltx/__pycache__ ../pyltx/pyltx.egg* ../setup.py
make html