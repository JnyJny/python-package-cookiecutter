# Python Package Cookiecutter Template

There are many [cookiecutter][cookiecutter] [templates][templates],
but this one is mine. Using this template, you can quickly create a
skeleton Python package with a command-line interface implemented in
typer.

## Features

- Auto detects user name and email from .gitconfig or environment.
- Creates a virtual environment in the project root.
- Exposes a command line interface built with typer.
- Package is callable via "python -m <package>".
- Automatically syncs deps and project into virtual environment.
- Automatically initializes a git repository with a main branch.
- Automatically activated virtual environments via .envrc.
- [Poe the Poet][poe] tasks integrated into pyproject.toml:
  - Test with pytest.
  - Generate HTML code coverage reports.
  - Run code quality checks: mypy/ruff/ty
  - Publish to PyPI via GitHub Actions.

## Prerequisites

These tools are expected to be available in your development
environment:

- [git][git]
- [uv][uv]
- [cookiecutter][cookiecutter]
- [direnv][direnv] _optional_

## Usage

Presuming you have uv installed, you get uvx for free!

```console
uvx cookiecutter gh:JnyJny/python-package-cookiecutter
```


[cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/index.html
[templates]: https://www.cookiecutter.io/templates
[poe]: https://poethepoet.natn.io
[git]: https://git-scm.com/downloads
[uv]: https://docs.astral.sh/uv/
[direnv]: https://direnv.net

