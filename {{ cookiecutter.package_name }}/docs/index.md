# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Overview

{{ cookiecutter.project_name }} is a Python package that provides a command-line interface for [brief description of what your package does].

## Quick Start

Install {{ cookiecutter.package_name }} using pip:

```bash
pip install {{ cookiecutter.package_name }}
```

Then run the CLI:

```bash
{{ cookiecutter.cli_name }} --help
```

## Features

- Modern Python packaging with `uv` support
- CLI interface built with Typer
- Structured logging with Loguru
{% if cookiecutter.use_pydantic_settings -%}
- Configuration management with Pydantic Settings
{% endif -%}
- Type checking with ty
- Code quality tools (ruff, pytest)
- Automated testing and CI/CD

## Installation

For detailed installation instructions, see [Installation](getting-started/installation.md).

## Documentation

- [Getting Started](getting-started/quickstart.md) - Quick start guide
- [User Guide](user-guide/cli.md) - Detailed usage instructions
- [API Reference](reference/) - Complete API documentation
- [Contributing](contributing.md) - How to contribute to this project

## License

{% if cookiecutter.license != 'no-license' -%}
This project is licensed under the {{ cookiecutter.license }} license.
{% else -%}
This project is not licensed.
{% endif -%}

## Support

- [GitHub Issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/issues)
- [GitHub Repository](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }})