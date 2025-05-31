# Python Package Cookiecutter Template

There are many [cookiecutter][cookiecutter] [templates][templates],
but this one is mine. Using this template, you can quickly create a
skeleton Python package with a command-line interface implemented in
typer.

## Features

- Tries to auto detects user name and email from .gitconfig or environment
- Creates a virtual environment in the project root [.venv]
- Exposes a command line interface built with typer.
- Package is callable via "python -m <package>" 
- Automatically activated virtual environments via .envrc and direnv
- Automatically syncs deps and project into virtual environment
- Automatically initializes a git repository with a main branch
- [poethepoet][poe] tasks integrated into pyproject.toml:
  - Test with pytest.
  - Generate HTML code coverage reports.
  - Run code quality checks: mypy/ruff/ty
  - Publish to PyPI via GitHub Actions.

## Prerequisites
- [uv][uv]
- [cookiecutter][cookiecutter]
- [direnv][direnv] _optional_

## Usage

Presuming you have uv installed, you get uvx for free!

```console
uvx cookiecutter hg:JnyJny/python-package-cookiecutter
```



[cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/index.html
[templates]: https://www.cookiecutter.io/templates
[uv]: https://docs.astral.sh/uv/
[direnv]: https://direnv.net
[poe]: https://poethepoet.natn.io
