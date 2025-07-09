# CLI Usage

{{ cookiecutter.project_name }} provides a command-line interface built with Typer.

## Basic Syntax

```bash
{{ cookiecutter.cli_name }} [OPTIONS] [COMMAND] [ARGS]...
```

## Global Options

The following options are available for all commands:

- `--help`: Show help message and exit
- `--version`: Show version and exit

## Commands

### Help

Get help for the CLI or any specific command:

```bash
{{ cookiecutter.cli_name }} --help
{{ cookiecutter.cli_name }} [command] --help
```

### Version

Display the version:

```bash
{{ cookiecutter.cli_name }} --version
```

## Self-Subcommands

{{ cookiecutter.project_name }} uses a self-subcommand pattern, where the main command can also act as a subcommand. This provides a clean and intuitive interface.

## Logging

The CLI uses structured logging with Loguru. You can control the log level using:

```bash
{{ cookiecutter.cli_name }} --log-level DEBUG [command]
```

{% if cookiecutter.log_to_file -%}
## Log Files

By default, logs are also written to `{{ cookiecutter.package_name }}.log` in the current directory.
{% endif -%}

## Examples

For specific usage examples, see the [Examples](examples.md) page.

## Error Handling

The CLI provides clear error messages and appropriate exit codes:

- `0`: Success
- `1`: General error
- `2`: Command line usage error

## Shell Completion

{{ cookiecutter.project_name }} supports shell completion for bash, zsh, and fish. To enable it:

### Bash

```bash
eval "$(_{{ cookiecutter.cli_name.upper() }}_COMPLETE=bash_source {{ cookiecutter.cli_name }})"
```

### Zsh

```bash
eval "$(_{{ cookiecutter.cli_name.upper() }}_COMPLETE=zsh_source {{ cookiecutter.cli_name }})"
```

### Fish

```bash
eval "$(_{{ cookiecutter.cli_name.upper() }}_COMPLETE=fish_source {{ cookiecutter.cli_name }})"
```