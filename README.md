<h3 align="center">Copier django template</h3>

<p align="center">
    <img width="500"
         src="https://raw.githubusercontent.com/savilard/django-boilerplate/main/assets/readme.png"
         alt="Books library restyle" />
</p>

<p align="center">
  <img alt="Codeclimate" src="https://img.shields.io/codeclimate/maintainability/savilard/django-boilerplate?style=for-the-badge">
  <img alt="Platform" src="https://img.shields.io/badge/platform-linux-green?style=for-the-badge" />
  <img alt="Python version" src="https://img.shields.io/badge/python-3.9-green?style=for-the-badge" />
  <a href="https://github.com/wemake-services/wemake-python-styleguide"><img src="https://img.shields.io/badge/style-wemake-blue?style=for-the-badge" alt="Code style"></a>
</p>

## Contents

<!-- TOC -->
* [Purpose](#purpose)
* [Features](#features)
* [Installation](#installation)
* [Resources](#resources)
* [Issues](#issues)
* [License](#license)
<!-- TOC -->
## Purpose

This project is used to scaffold a `django` project structure.
Just like `django-admin.py startproject` but better.


## Features

* API-only django based on Django REST Framework
* Supports latest `python3.9+`
* [`poetry`](https://github.com/python-poetry/poetry) for managing dependencies
* [`mypy`](https://mypy.readthedocs.io), [`django-stubs`](https://github.com/typeddjango/django-stubs) and [`djangorestframework-stubs`](https://github.com/typeddjango/djangorestframework-stubs) for static typing
* [`pytest`](https://pytest.org/) for unit tests
* [`flake8`](http://flake8.pycqa.org/en/latest/) and [`wemake-python-styleguide`](https://wemake-python-styleguide.readthedocs.io/en/latest/) for linting
* [`docker`](https://www.docker.com/) for development
* [`github actions`](https://github.com/features/actions) for CI
* Custom [`user model`](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model)


## Installation

Firstly, you will need to install [dependencies](https://copier.readthedocs.io/en/stable/#installation):
```shell
pip install pipx
pipx install copier
```

Then, create a project itself:
```shell
copier gh:savilard/django-boilerplate project_folder_name
```


## Resources

Please consult the [Copier](https://copier.readthedocs.io/en/stable/) docs for more information.


## Issues
If you encounter any problems, please [file an issue](https://github.com/savilard/django-boilerplate/issues) along with a detailed description.


## License
MIT. See [LICENSE](https://github.com/savilard/django-boilerplate/blob/main/LICENSE) for more details.
