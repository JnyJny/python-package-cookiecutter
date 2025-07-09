# Configuration

{% if cookiecutter.use_pydantic_settings -%}
{{ cookiecutter.project_name }} uses Pydantic Settings for configuration management, which allows you to configure the application using environment variables, configuration files, or both.

## Environment Variables

You can configure {{ cookiecutter.package_name }} using environment variables:

```bash
export {{ cookiecutter.package_name.upper() }}_SETTING_NAME=value
{{ cookiecutter.cli_name }} [command]
```

## Configuration File

You can also use a configuration file. Create a `.env` file in your project directory:

```bash
# .env
{{ cookiecutter.package_name.upper() }}_SETTING_NAME=value
```

## Available Settings

The following settings are available:

### Logging Settings

- `{{ cookiecutter.package_name.upper() }}_LOG_LEVEL`: Set the logging level (default: INFO)
{% if cookiecutter.log_to_file -%}
- `{{ cookiecutter.package_name.upper() }}_LOG_FILE`: Path to log file (default: {{ cookiecutter.package_name }}.log)
{% endif -%}

### Application Settings

Add your application-specific settings here.

## Priority Order

Settings are loaded in the following priority order (highest to lowest):

1. Environment variables
2. Configuration file (`.env`)
3. Default values

## Example

```bash
# Set log level to DEBUG
export {{ cookiecutter.package_name.upper() }}_LOG_LEVEL=DEBUG

# Run the CLI
{{ cookiecutter.cli_name }} [command]
```

{% else -%}
{{ cookiecutter.project_name }} uses simple configuration through command-line arguments and environment variables.

## Environment Variables

You can configure logging using environment variables:

```bash
export LOG_LEVEL=DEBUG
{{ cookiecutter.cli_name }} [command]
```

## Command Line Options

Most configuration is done through command-line arguments. Use the `--help` flag to see available options:

```bash
{{ cookiecutter.cli_name }} --help
```

{% endif -%}