[![gh:JnyJny/python-package-cookiecutter][python-package-cookiecutter-badge]][python-package-cookiecutter] 
[![releases][release-badge]][releases] 
[![test-status][test-status-badge]][testing-workflow]

# Python Package Cookiecutter Template

There are many [cookiecutter][cookiecutter] [templates][templates],
but this one is mine and I'm sharing it with you. Create complete Python 
packages with zero configuration - including CLI, testing, documentation, 
and automated PyPI publishing via GitHub Actions.

## Features

- **Zero Configuration CI/CD** - Complete GitHub Actions workflows for testing, 
  building, and publishing to PyPI
- **CLI Ready** - [Typer](https://typer.tiangolo.com) CLI with help and autocompletion
- **Fast Dependencies** - [uv](https://docs.astral.sh/uv/) for lightning-fast package management
- **Quality Tools** - Pre-configured ruff, ty, pytest, and coverage reporting
- **Documentation** - [MkDocs](https://www.mkdocs.org/) with auto-deployment to GitHub Pages
- **Flexible** - Optional Pydantic settings, multiple build backends, cross-platform testing

## Quick Start

### Create Your Project

```console
# With uvx (recommended)
uvx cookiecutter gh:JnyJny/python-package-cookiecutter

# Or with pip
pip install cookiecutter
cookiecutter gh:JnyJny/python-package-cookiecutter
```

### Start Developing

```console
cd your-new-project
poe --help          # See all available tasks
poe qc              # Run quality checks
poe test            # Run tests
poe publish_patch   # Release to PyPI
```

**That's it!** Your package is now live on PyPI with documentation deployed to 
GitHub Pages.

## Documentation

For detailed information, see the complete documentation:

📚 **[https://jnyjny.github.io/python-package-cookiecutter/](https://jnyjny.github.io/python-package-cookiecutter/)**

- **[Overview](https://jnyjny.github.io/python-package-cookiecutter/overview/)** - Template features and benefits
- **[Quick Start](https://jnyjny.github.io/python-package-cookiecutter/quickstart/)** - Step-by-step getting started guide  
- **[Template Guide](https://jnyjny.github.io/python-package-cookiecutter/template-guide/)** - Detailed feature documentation
- **[Customization](https://jnyjny.github.io/python-package-cookiecutter/customization/)** - How to modify your generated project

## Contributing

Found a bug or want to contribute? Please see our [Contributing Guidelines](CONTRIBUTING.md) and feel free to open an issue or pull request.

## License

This template is released under the Apache License 2.0. Generated projects use the license you choose during template creation.

<!-- Links -->
[python-package-cookiecutter-badge]: https://img.shields.io/badge/Made_With_Cookiecutter-python--package--cookiecutter-green?style=for-the-badge
[python-package-cookiecutter]: https://github.com/JnyJny/python-package-cookiecutter
[release-badge]: https://img.shields.io/github/v/release/JnyJny/python-package-cookiecutter?sort=semver&display_name=tag&style=for-the-badge&color=green
[releases]: https://github.com/JnyJny/python-package-cookiecutter/releases
[test-status-badge]: https://img.shields.io/github/actions/workflow/status/JnyJny/python-package-cookiecutter/release.yaml?style=for-the-badge&label=Tests
[testing-workflow]: https://github.com/JnyJny/python-package-cookiecutter/actions/workflows/release.yaml
[cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/index.html
[templates]: https://www.cookiecutter.io/templates
