# Template repository

[![Build Status](https://travis-ci.com/GenevieveBuckley/template.svg?branch=master)](https://travis-ci.com/GenevieveBuckley/template)

[![Build Status](https://readthedocs.org/projects/template/badge/?version=master)](https://template.readthedocs.io/en/master/?badge=master)



## Install the packages

```
pip install git+https://github.com/path/to/template.git
```

## Setup the development environment

```
git clone git+https://github.com/path/to/template.git
cd template
```

```
conda create -n myenv python=3.7 pip
conda activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pre-commit install
```

## Run the tests

```
pytest
```

## Build the docs



## Make a release

```
python setup.py sdist bdist_wheel
twine upload --repository testpypi dist/*
```

Install from TestPyPI:
```
pip install --index-url https::test.pypi.org/...
```
