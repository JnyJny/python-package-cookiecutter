{%- if cookiecutter.readme_badges == "yes" %}
[![Release][badge-release]][release]
![Version][badge-pypi-version]
![Release Date][badge-release-date]
![Python Version][badge-python-version]
![License][badge-license]
![Monthly Downloads][badge-monthly-downloads]
{% endif -%}
# {{ cookiecutter.package_name }} - {{ cookiecutter.project_name }}

> {{ cookiecutter.project_short_description }}

<!-- project description -->

## Features

<!-- project features --> 

## Installation

### pip

```console
python3 -m pip install {{ cookiecutter.package_name }}
```

### uvx
```console
uvx --from {{ cookiecutter.package_name }} {{ cookiecutter.cli_name }}
```

### uv

```console
uvx pip install {{ cookiecutter.package_name }}
```

## Usage

```console
{{ cookiecutter.cli_name }} --help
```


## Development

This project and it's virtual environment is managed using [uv][uv] and
is configured to support automatic activation of virtual environments
using [direnv][direnv]. Development activites such as linting and testing
are automated via [Poe The Poet][poethepoet], run `poe` after cloning
this repo.

### Clone
```console
git clone {{ cookiecutter.repository }}
cd {{ cookiecutter.package_name }}
```
### Allow Direnv _optional_ but recommended
```console
direnv allow
```

### Create a Virtual Environment
```console
uv venv
```
### Install Dependencies
```console
uv sync
```
### Run `poe`
```console
poe --help
```

<hr>

[![gh:JnyJny/python-package-cookiecutter][python-package-cookiecutter-badge]][python-package-cookiecutter]

<!-- End Links -->

[python-package-cookiecutter-badge]: https://img.shields.io/badge/Made_With_Cookiecutter-python--package--cookiecutter-green?style=for-the-badge
[python-package-cookiecutter]: https://github.com/JnyJny/python-package-cookiecutter
{% if cookiecutter.readme_badges == "yes" -%}
[badge-release]: {{ cookiecutter.repository }}/actions/workflows/release.yaml/badge.svg
[release]: {{ cookiecutter.repository }}/actions/workflows/release.yaml
[badge-pypi-version]: https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}
[badge-release-date]: https://img.shields.io/github/release-date/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}
[badge-python-version]: https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2F{{cookiecutter.github_username }}%2F{{ cookiecutter.package_name }}%2Fmain%2Fpyproject.toml
[badge-license]: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}
[badge-monthly-downloads]: https://img.shields.io/pypi/dm/{{ cookiecutter.package_name }}
{% endif -%}
[poe]: https://poethepoet.natn.io
[uv]: https://docs.astral.sh/uv/
[direnv]: https://direnv.net
