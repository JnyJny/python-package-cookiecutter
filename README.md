[![gh:JnyJny/python-package-cookiecutter][python-package-cookiecutter-badge]][python-package-cookiecutter]

# Python Package Cookiecutter Template

There are many [cookiecutter][cookiecutter] [templates][templates],
but this one is mine. With it, you can quickly create a full-featured
Python package designed to be managed with [uv][uv], a default
[typer][typer] command-line interface, and logging using my favorite
logger, [loguru][loguru].

## Features

- Python project designed to be managed with [uv][uv].
- Auto detects user name and email from .gitconfig or environment.
- Creates a virtual environment in the project directory.
- Exposes a command line interface built with [typer][typer].
- Package is callable via `python -m <package>`.
- Automatically syncs deps and project into virtual environment.
- Automatically initializes a git repository with a main branch.
- Automatically activated virtual environments via .envrc.
- [Poe the Poet][poe] tasks integrated into pyproject.toml:
  - Test with pytest.
  - Generate HTML code coverage reports.
  - Run code quality checks using mypy, ruff, and ty
  - Publish to PyPI via GitHub Actions with `poe publish`
- Tool options integrated into pyproject.toml.
- Optionally configured badges in README.md.

## Prerequisites

### User Accounts
- GitHub account
- PyPI account

### Required Tools
- [git][git]
- [uv][uv]
- [cookiecutter][cookiecutter] via uvx

### _Optional_ but Recommended Tools
- [direnv][direnv]
- [gh][gh]

## Usage

### Initial Project Creation

Once you have uv installed, you get uvx for free!

```console
uvx cookiecutter gh:JnyJny/python-package-cookiecutter
```

### Example Package Tree
```console

```

### Post Install

If you have [direnv][direnv] installed, your project's virtual
environment will be activated when you enter the project directory
or sub-directories. Without direnv, you can activate the project
virtual environment manually with `source .venv/bin/activate`.

Once your venv is activated, all the dev tools are available for use
without having to use `uv run` to preface the command.


#### Default Poe Tasks 

```console

```

#### Example Workflow

1. Create project from template
1. Edit package to suit yourself.
1. Commit and push changes to your repo.
1. Publish a patch release using `poe publish`.

### Things You Will Want to Change

#### .github/workflows/release.yml

The `release.yaml` workflow defines a matrix of operating systems and
Python versions to test against. Tests are run when a semantic
versioning tag or a tag with the suffix "-test" is pushed to a branch.

In it's initial state, tests are run against Linux, MacOS, and Windows
for Python versions 3.9, 3.10, 3.11, 3.12 and 3.13. This will
result in 15 seperate test instances that need to succeed before
the publish stage of release will start. Chances are very good
you don't need that sort of rigor in testing, so feel free to
trim the os and python-version lists to fit your needs.


## TODO
- Automatic github repo creation [optional]
- Automatic GitHub release creation in release workflow.
- Automatic release notes generator
- Integration with readthedocs.io
- 




<!-- End Links -->
[python-package-cookiecutter-badge]: https://img.shields.io/badge/Cookiecutter-gh%3AJnyJny%2Fpython-package-cookiecutter
[python-package-cookiecutter]: https://github.com/JnyJny/python-package-cookiecutter

[cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/index.html
[templates]: https://www.cookiecutter.io/templates
[poe]: https://poethepoet.natn.io
[git]: https://git-scm.com/downloads
[uv]: https://docs.astral.sh/uv/
[direnv]: https://direnv.net
[typer]: https://typer.tiangolo.com
[loguru]: https://loguru.readthedocs.io/en/stable/

