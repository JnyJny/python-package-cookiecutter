# Python Package Cookiecutter Template - Overview

## What is this template?

There are many [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html) 
[templates](https://www.cookiecutter.io/templates), but this one is mine and I'm sharing 
it with you. With it, you can quickly create a full-featured Python package designed to 
be managed with [uv](https://docs.astral.sh/uv/) and 
[direnv](https://direnv.net), a default [typer](https://typer.tiangolo.com) 
command-line interface, optional settings using 
[pydantic-settings](https://docs.pydantic.dev/latest/api/pydantic_settings/) and 
logging using my favorite logger, [loguru](https://loguru.readthedocs.io/en/stable/). 
Development activities like testing, code quality checks, and publishing to PyPI are 
all baked in and ready to go thanks to [Poe The Poet](https://poethepoet.natn.io). 
Project documentation is automatically configured to deploy to GitHub Pages using 
[MkDocs](https://www.mkdocs.org/). Best of all, I've added all sorts of templates and 
base files to help provide a great GitHub experience for you and people that interact 
with your project repository.

## Why Use This Template?

### Zero Configuration Required
- **Complete CI/CD pipeline** with GitHub Actions for testing, building, and publishing
- **Automated PyPI publishing** with trusted publishing (no API tokens needed)
- **Documentation** auto-deployed to GitHub Pages
- **Quality tools pre-configured**: ruff, ty, pytest, coverage reporting

### Python Ecosystem
- **[uv](https://docs.astral.sh/uv/)** for lightning-fast dependency management and 
  Python version control
- **[Typer](https://typer.tiangolo.com)** CLI framework with rich help and autocompletion
- **[Loguru](https://loguru.readthedocs.io/en/stable/)** for beautiful, structured logging
- **[Pydantic Settings](https://docs.pydantic.dev/latest/api/pydantic_settings/)** for 
  configuration management
- **[MkDocs](https://www.mkdocs.org/)** with multiple theme options for documentation

### Package Structure
- **src/ layout** following Python packaging best practices
- **Comprehensive testing** setup with pytest and coverage
- **Multiple build backends** (uv or hatch) 
- **Semantic versioning** with automated changelog generation
- **Cross-platform testing** (Linux, macOS, Windows)

### Seamless Workflow
- **Write Code** - Edit your package source files
- **Quality Control** - Run `poe qc` to check code quality
- **Release** - Run `poe publish` to version and tag
- **Live on PyPI** - Automatic publishing via GitHub Actions

## What You Get

When you create a project with this template, you get:

### Project Structure
```
your-package/
├── .github/              # GitHub workflows and templates
│   ├── workflows/
│   │   ├── release.yaml  # Complete CI/CD pipeline
│   │   └── docs.yml      # Documentation deployment
│   └── ISSUE_TEMPLATE/   # Issue and PR templates
├── docs/                 # MkDocs documentation
├── src/your_package/     # Your package source code
│   ├── __init__.py
│   ├── __main__.py       # CLI entry point
│   ├── self_subcommand.py
│   └── settings.py       # Optional configuration
├── tests/                # Test suite
├── pyproject.toml        # Project configuration
├── README.md             # Project documentation
└── LICENSE               # Your chosen license
```

### Built-in Tools
- **Testing**: pytest with coverage reporting
- **Code Quality**: ruff for linting and formatting, ty for type checking
- **Documentation**: MkDocs with auto-generated API docs
- **Task Runner**: Poe The Poet for common development tasks
- **Dependency Management**: uv for fast, reliable dependency resolution
- **Version Control**: Git with automatic initial commit
- **CI/CD**: Complete GitHub Actions workflows

### GitHub Integration
- **Issue Templates**: Bug reports, feature requests, and questions
- **Pull Request Template**: Contribution guidelines
- **Dependabot**: Automatic dependency updates
- **Release Automation**: Semantic versioning with auto-generated changelogs
- **Documentation Deployment**: Automatic GitHub Pages deployment

## Template Configuration

The template is highly configurable through cookiecutter prompts:

### Required Configuration
- **Package Name**: Your Python package name
- **Project Description**: Brief description of your project
- **Author Information**: Your name and email
- **License**: Choose from multiple open source licenses

### Optional Features
- **Pydantic Settings**: Configuration management with environment variables
- **File Logging**: Optional file-based logging in addition to console
- **GitHub Repository**: Automatic repository creation and push
- **Build Backend**: Choose between uv or hatch
- **Documentation Theme**: Multiple MkDocs theme options

### CI/CD Configuration
- **Python Version Matrix**: Which Python versions to test against
- **OS Matrix**: Which operating systems to test on
- **Testing Strategy**: Comprehensive test matrix or minimal testing

## Next Steps

- [Quick Start Guide](quickstart.md) - Get started in minutes
- [Template User Guide](template-guide.md) - Detailed feature documentation
- [Customization Guide](customization.md) - How to modify your generated project

## Support

- **GitHub Issues**: Report bugs or request features
- **Discussions**: Ask questions and share ideas
- **Contributing**: See CONTRIBUTING.md for contribution guidelines