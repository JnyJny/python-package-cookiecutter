# Contributing

We welcome contributions to {{ cookiecutter.project_name }}! This guide will help you get started.

## Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/YOUR_USERNAME/{{ cookiecutter.package_name }}.git
cd {{ cookiecutter.package_name }}
```

3. Install dependencies using `uv`:

```bash
uv sync
```

4. Install pre-commit hooks:

```bash
uv run pre-commit install
```

## Development Workflow

### Code Quality

We use several tools to maintain code quality:

```bash
# Run all code quality checks
uv run poe check

# Or run individual tools
uv run poe ruff      # Linting and formatting
uv run poe mypy      # Type checking
uv run poe ty        # Additional type checking
```

### Testing

Run the test suite:

```bash
uv run poe test
```

Run tests with coverage:

```bash
uv run poe coverage
```

### Documentation

Build and serve the documentation locally:

```bash
uv run mkdocs serve
```

The documentation will be available at `http://localhost:8000`.

## Making Changes

1. Create a new branch for your feature or bugfix:

```bash
git checkout -b feature/your-feature-name
```

2. Make your changes, ensuring you:
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed
   - Keep commits focused and well-described

3. Run the full test suite:

```bash
uv run poe qc
```

4. Commit your changes:

```bash
git add .
git commit -m "Add your descriptive commit message"
```

5. Push to your fork:

```bash
git push origin feature/your-feature-name
```

6. Create a Pull Request on GitHub

## Code Style

- We use `ruff` for linting and formatting
- Follow PEP 8 guidelines
- Use type hints for all functions and methods
- Write docstrings for all public functions and classes
- Keep functions focused and reasonably sized

## Testing Guidelines

- Write tests for all new functionality
- Use descriptive test names
- Test both positive and negative cases
- Use fixtures for common test data
- Mock external dependencies

## Documentation

- Update documentation for any API changes
- Add examples for new features
- Keep documentation clear and concise
- Use proper markdown formatting

## Submitting Changes

### Pull Request Process

1. Ensure your PR description clearly describes the problem and solution
2. Include the relevant issue number if applicable
3. Make sure all tests pass and code quality checks pass
4. Request review from maintainers
5. Address any feedback promptly

### Commit Messages

Use clear, descriptive commit messages:

```
Add support for configuration files

- Implement ConfigLoader class
- Add tests for configuration loading
- Update documentation with examples
```

## Release Process

Releases are managed by maintainers using the following commands:

```bash
# Patch release (bug fixes)
uv run poe publish_patch

# Minor release (new features)
uv run poe publish_minor

# Major release (breaking changes)
uv run poe publish_major
```

## Getting Help

- Create an issue on GitHub for bugs or feature requests
- Join discussions in existing issues
- Reach out to maintainers for guidance

## Code of Conduct

Please be respectful and constructive in all interactions. We want to maintain a welcoming environment for all contributors.

## License

By contributing to {{ cookiecutter.project_name }}, you agree that your contributions will be licensed under the same license as the project.

## Recognition

Contributors will be recognized in the project's README and release notes.

Thank you for contributing to {{ cookiecutter.project_name }}!