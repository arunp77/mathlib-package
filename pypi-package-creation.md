# Step to create a python package on pypi


## **Configure Your Package for PyPI**

Ensure that your `setup.py` or `pyproject.toml` file is properly configured to include the `README.md` file.

**For `setup.py`:**

```python
from setuptools import setup, find_packages

setup(
    name='mathlib',
    version='0.1',
    packages=find_packages(),
    description='A simple math library with basic operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Arun Kumar Pandey',
    author_email='arunp77@gmail.com',
    url='https://github.com/arunp77/Data-engineering-tools/matlib',
    license='MIT',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
```

**For `pyproject.toml` with Poetry:**

```toml
[tool.poetry]
name = "your-package-name"
version = "0.1.0"
description = "A brief description of your package"
readme = "README.md"
authors = ["Your Name <your.email@example.com>"]
license = "MIT"

[tool.poetry.dependencies]
# List your package dependencies here
```

## **Build Your Package**

Before uploading to PyPI, build your package (but first install the following package: `pip install wheel twine`) and then go to:

```bash
python setup.py sdist bdist_wheel
```

Or if using Poetry:

```bash
poetry build
```

## **Upload to PyPI**

Upload your package to PyPI using Twine:

```bash
twine upload dist/*
```

### 6. **Verify Your Package**

After uploading, you can verify your package on PyPI by visiting the [PyPI website](https://pypi.org) and searching for your package name. Ensure that the `README.md` content appears correctly.

My package is available at: [https://pypi.org/project/arunp77-mathlib/](https://pypi.org/project/arunp77-mathlib/).