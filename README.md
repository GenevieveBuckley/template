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

## Continuous integration services

* https://travis-ci.com
* https://coveralls.io/repos/new


## Build the docs
1. Run `sphinx-quickstart` from within the `docs/` folder:

```
mkdir docs
cd docs
sphinx-quickstart
```
Answer the questions for package name, author, etc. Use the default values.

2. Configure the path to the root directory
Open `docs/source/conf.py` and configure the path to the root directory.

From this...
```python
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
```

To this instead...
```python
import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # <--- THIS BIT ALSO CHANGED!
```

3. Add sphinx extensions
Open `docs/source/conf.py` and add these sphinx extensions to the list:

```python
extensions = ['m2r',
              'sphinx.ext.autodoc',
              'sphinx.ext.coverage',
              'sphinx.ext.napoleon',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
]
```


4. Build the html documentation
```
cd docs/
sphinx-apidoc -o source/ ../mypackage
make html
```

5. Host the docs on GitHub pages
In the GitHub repository settings, enable github pages.
```
git commit docs/_build/*
git push origin gh-pages
```

Read more about sphinx:
* https://medium.com/@eikonomega/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365
* https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b
* https://sphinx-rtd-tutorial.readthedocs.io/en/latest/index.html
* https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-ii-6/

## Automate publishing documentation updates


Resources:
* https://amarder.github.io/using-travis-ci-to-build-sphinx-docs/
* https://docs.travis-ci.com/user/deployment/pages/#Setting-the-GitHub-token

## Make a release

1. Increment the version number in `_version.py`

2. Go to the 'Releases' tab on GitHub and create a new release tag

3. Make the binary files to upload:
```
python setup.py sdist bdist_wheel
```

4. (Optioaal) Upload your new release to TestPyPI
```
twine upload --repository testpypi dist/*
```
Check the install from TestPyPI:
```
pip install --index-url https::test.pypi.org/...
```

5. (Optional) Upload your new release to PyPI
```
twine upload --repository pypi dist/*
```

See resources:
* https://2019.pycon-au.org/talks/shipping-your-first-python-package-and-automating-future-publishing
* https://medium.com/mobileforgood/5-tips-to-optimise-your-travis-ci-file-eced09d2d74e
