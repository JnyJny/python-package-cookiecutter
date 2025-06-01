{% if cookiecutter.readme_badges %}
[![Release][badge-release]][release]
![Version][badge-pypi-version]
![Release Date][badge-release-date]
![Python Version][badge-python-version]
![License][badge-license]
![Black][badge-black]
![Monthly Downloads][badge-monthly-downloads]
{% endif %}

# {{ cookiecutter.package_name }} - {{ cookiecutter.project_name }}

> {{ cookiecutter.project_short_description }}

<!-- description -->

## Installation

## Usage

## Contact

[![gh:JnyJny/python-package-cookiecutter][python-package-cookiecutter-badge]][python-package-cookiecutter]

<!-- End Links -->

[python-package-cookiecutter-badge]: https://img.shields.io/badge/Cookiecutter-gh%3AJnyJny%2Fpython-package-cookiecutter
[python-package-cookiecutter]: https://github.com/JnyJny/python-package-cookiecutter
{% if cookiecutter.readme_badges %}
[badge-release]: {{ cookiecutter.repository }}/actions/workflows/release.yaml/badge.svg
[badge-pypi-version]: https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}
[badge-python-version]: https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2F{{cookiecutter.github_username }}%2F{{ cookiecutter.package_name }}%2Fmain%2Fpyproject.toml
[badge-license]: https://img.shields.io/pypi/l/{{ cookiecutter.package_name }}
[badge-black]: https://img.shields.io/badge/code%20style-black-000000.svg
[badge-monthly-downloads]: https://img.shields.io/pypi/dm/{{ cookiecutter.package_name }}
{% endif %}
