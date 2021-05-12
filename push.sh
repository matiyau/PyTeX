rm -rf dist
pipreqs --no-pin --force
python3 -m build
twine upload dist/*
