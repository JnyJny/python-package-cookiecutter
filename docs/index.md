# Python Package Cookiecutter Template Documentation

Welcome to the comprehensive documentation for the Python Package Cookiecutter Template.

## Getting Started

### New to the Template?
- **[Overview](overview.md)** - Learn what this template offers and why you should use it
- **[Quick Start](quickstart.md)** - Get your first package running in minutes

### Ready to Dive Deeper?
- **[Template User Guide](template-guide.md)** - Detailed documentation of all features
- **[Customization Guide](customization.md)** - How to modify your generated project

## What This Template Provides

### Zero Configuration CI/CD
- Complete GitHub Actions workflows for testing, building, and publishing
- Automated PyPI publishing with trusted publishing (no API tokens needed)
- Documentation auto-deployed to GitHub Pages
- Quality tools pre-configured: ruff, ty, pytest, coverage reporting

### Python Ecosystem
- **[uv](https://docs.astral.sh/uv/)** for fast dependency management
- **[Typer](https://typer.tiangolo.com)** CLI framework with rich help
- **[Loguru](https://loguru.readthedocs.io/en/stable/)** for structured logging
- **[Pydantic Settings](https://docs.pydantic.dev/latest/api/pydantic_settings/)** for configuration
- **[MkDocs](https://www.mkdocs.org/)** with multiple theme options

### Package Structure
- **src/ layout** following Python packaging best practices
- **Comprehensive testing** setup with pytest and coverage
- **Multiple build backends** (uv or hatch)
- **Semantic versioning** with automated changelog generation
- **Cross-platform testing** (Linux, macOS, Windows)

## Quick Navigation

| I want to... | Go to... |
|---------------|-----------|
| **Understand what this template offers** | [Overview](overview.md) |
| **Create my first package quickly** | [Quick Start](quickstart.md) |
| **Learn about all features in detail** | [Template User Guide](template-guide.md) |
| **Customize my generated project** | [Customization Guide](customization.md) |
| **See examples and best practices** | [Template User Guide - Examples](template-guide.md#configuration-options) |
| **Understand the GitHub workflows** | [Template User Guide - GitHub Actions](template-guide.md#github-actions-workflow-details) |
| **Set up PyPI publishing** | [Template User Guide - Trusted Publishing](template-guide.md#trusted-publishing-setup) |

## Template Workflow

The template enables a streamlined development workflow:

1. **Write Code** - Edit your package source files
2. **Quality Control** - Run `poe qc` to check code quality
3. **Release** - Run `poe publish` to version and tag
4. **Live on PyPI** - Automatic publishing via GitHub Actions

## Example Generated Project Structure

```
your-package/
├── .github/workflows/     # Complete CI/CD pipeline
├── docs/                  # MkDocs documentation
├── src/your_package/      # Your source code
│   ├── __main__.py        # CLI entry point
│   └── settings.py        # Configuration (optional)
├── tests/                 # Comprehensive test suite
├── pyproject.toml         # Project configuration
├── README.md              # Project documentation
└── LICENSE                # Your chosen license
```

## Support and Contributing

- **Issues**: Report bugs or request features on [GitHub Issues](https://github.com/JnyJny/python-package-cookiecutter/issues)
- **Discussions**: Ask questions on [GitHub Discussions](https://github.com/JnyJny/python-package-cookiecutter/discussions)
- **Contributing**: See the project's CONTRIBUTING.md for contribution guidelines

## License

This template is released under the Apache License 2.0. Generated projects use the license you choose during template creation.

---

**Ready to get started?** Head to the [Quick Start Guide](quickstart.md) to create your first package in minutes!