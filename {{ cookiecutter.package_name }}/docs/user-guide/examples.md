# Examples

This page provides practical examples of using {{ cookiecutter.project_name }}.

## Basic Usage

### Getting Help

```bash
# Show main help
{{ cookiecutter.cli_name }} --help

# Show help for a specific command
{{ cookiecutter.cli_name }} [command] --help
```

### Check Version

```bash
{{ cookiecutter.cli_name }} --version
```

## Advanced Usage

### Using with Different Log Levels

```bash
# Run with debug logging
{{ cookiecutter.cli_name }} --log-level DEBUG [command]

# Run with minimal logging
{{ cookiecutter.cli_name }} --log-level ERROR [command]
```

{% if cookiecutter.use_pydantic_settings -%}
### Using with Configuration

```bash
# Set configuration via environment variables
export {{ cookiecutter.package_name.upper() }}_SETTING_NAME=value
{{ cookiecutter.cli_name }} [command]

# Or create a .env file
echo "{{ cookiecutter.package_name.upper() }}_SETTING_NAME=value" > .env
{{ cookiecutter.cli_name }} [command]
```
{% endif -%}

## Common Workflows

### Example Workflow 1

```bash
# Step 1: Initialize
{{ cookiecutter.cli_name }} init

# Step 2: Process
{{ cookiecutter.cli_name }} process --input file.txt

# Step 3: Output
{{ cookiecutter.cli_name }} output --format json
```

### Example Workflow 2

```bash
# One-liner example
{{ cookiecutter.cli_name }} process --input file.txt --output result.txt --verbose
```

## Error Handling Examples

### Common Errors

```bash
# File not found
{{ cookiecutter.cli_name }} process --input nonexistent.txt
# Error: Input file 'nonexistent.txt' not found

# Invalid option
{{ cookiecutter.cli_name }} --invalid-option
# Error: No such option: --invalid-option
```

### Debugging

```bash
# Run with debug logging to troubleshoot
{{ cookiecutter.cli_name }} --log-level DEBUG process --input file.txt
```

## Integration Examples

### Use in Scripts

```bash
#!/bin/bash
set -e

# Check if {{ cookiecutter.package_name }} is installed
if ! command -v {{ cookiecutter.cli_name }} &> /dev/null; then
    echo "{{ cookiecutter.package_name }} is not installed"
    exit 1
fi

# Run the command
{{ cookiecutter.cli_name }} process --input "$1" --output "$2"
echo "Processing complete"
```

### Use with Make

```makefile
.PHONY: process
process:
	{{ cookiecutter.cli_name }} process --input input.txt --output output.txt

.PHONY: clean
clean:
	rm -f output.txt {{ cookiecutter.package_name }}.log
```

## Performance Tips

- Use appropriate log levels in production
- Process files in batches when possible
- Use configuration files for repeated settings

## Next Steps

- Learn more about the [API Reference](../reference/)
- Check out the [Contributing Guide](../contributing.md)
- Visit the [GitHub repository](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }})