# Installation

{{ cookiecutter.project_name }} requires Python {{ cookiecutter.python_version_min }} or later.

## Install from PyPI

The easiest way to install {{ cookiecutter.package_name }} is from PyPI:

```bash
pip install {{ cookiecutter.package_name }}
```

## Install from Source

You can also install from source:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}.git
cd {{ cookiecutter.package_name }}
pip install -e .
```

## Development Installation

For development, we recommend using `uv`:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}.git
cd {{ cookiecutter.package_name }}
uv sync
```

This will install all dependencies including development tools.

## Verify Installation

After installation, verify that {{ cookiecutter.package_name }} is working:

```bash
{{ cookiecutter.cli_name }} --version
```

You should see the version number displayed.

## Next Steps

Now that you have {{ cookiecutter.package_name }} installed, check out the [Quick Start](quickstart.md) guide to learn how to use it.