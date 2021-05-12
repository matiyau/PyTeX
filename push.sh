rm -rf dist
pipreqs --no-pin --force
./docs/generate_docs.sh
python3 -m build
twine upload dist/*
