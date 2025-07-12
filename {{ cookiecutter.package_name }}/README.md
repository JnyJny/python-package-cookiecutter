{%- if cookiecutter.readme_badges %}
[![Release][badge-release]][release]
![Version][badge-pypi-version]
![Release Date][badge-release-date]
![Python Version][badge-python-version]
![License][badge-license]
![Monthly Downloads][badge-monthly-downloads]
{% endif -%}
# {{ cookiecutter.package_name }} - {{ cookiecutter.project_name }}

> {{ cookiecutter.project_short_description }}

## TL;DR

**Quick Start:**
```console
# Install
pip install {{ cookiecutter.package_name }}

# Run
{{ cookiecutter.cli_name }} --help
```

**What it does:** {{ cookiecutter.project_short_description }}

**Key features:** Modern Python CLI with type checking, testing, docs, and automated releases.

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

### Release Management

This project uses automated release management with GitHub Actions:

#### Version Bumping
- `poe publish_patch` - Bump patch version, commit, tag, and push
- `poe publish_minor` - Bump minor version, commit, tag, and push  
- `poe publish_major` - Bump major version, commit, tag, and push

#### Release Notes
- `poe changelog` - Generate changelog since last tag
- `poe release-notes` - Generate release notes file

#### Automatic Releases
When you push a version tag (e.g., `v1.0.0`), the unified GitHub Actions workflow will:
1. **Test** - Run tests across all supported Python versions and OS combinations
2. **Publish** - Build and publish to PyPI (only if tests pass)
3. **GitHub Release** - Create GitHub release with auto-generated notes and artifacts (only if PyPI publish succeeds)

This ensures a complete release pipeline where each step depends on the previous step's success.

#### MkDocs Documentation
- `poe docs-serve` - Serve documentation locally
- `poe docs-build` - Build documentation
- `poe docs-deploy` - Deploy to GitHub Pages

The template includes MkDocs with {{ cookiecutter.mkdocs_theme }} theme and automatic deployment to GitHub Pages.

<hr>

[![gh:JnyJny/python-package-cookiecutter][python-package-cookiecutter-badge]][python-package-cookiecutter]

<!-- End Links -->

[python-package-cookiecutter-badge]: https://img.shields.io/badge/Made_With_Cookiecutter-python--package--cookiecutter-green?style=for-the-badge
[python-package-cookiecutter]: https://github.com/JnyJny/python-package-cookiecutter
{% if cookiecutter.readme_badges -%}
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
