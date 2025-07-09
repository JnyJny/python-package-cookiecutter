# Quick Start

This guide will help you get started with {{ cookiecutter.project_name }} quickly.

## Basic Usage

After [installing](installation.md) {{ cookiecutter.package_name }}, you can use the CLI:

```bash
{{ cookiecutter.cli_name }} --help
```

This will show you all available commands and options.

## Common Commands

Here are some common commands to get you started:

### Help

Get help for any command:

```bash
{{ cookiecutter.cli_name }} --help
{{ cookiecutter.cli_name }} [command] --help
```

### Version

Check the version:

```bash
{{ cookiecutter.cli_name }} --version
```

{% if cookiecutter.use_pydantic_settings -%}
## Configuration

{{ cookiecutter.project_name }} can be configured using environment variables or a configuration file. See [Configuration](configuration.md) for details.
{% endif -%}

## Examples

For more detailed examples, see the [Examples](../user-guide/examples.md) page.

## Next Steps

- Learn more about the [CLI interface](../user-guide/cli.md)
- Check out the [API Reference](../reference/)
- Read the [Contributing Guide](../contributing.md) if you want to contribute