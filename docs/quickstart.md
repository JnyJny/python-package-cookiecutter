# Quick Start Guide

Get your Python package up and running in minutes with this cookiecutter template.

## Prerequisites

### Required Tools

| Tool | Required | Purpose |
|------|----------|---------|
| [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html) | ✅ | Creates projects from templates |
| [git](https://git-scm.com/downloads) | ✅ | Version control system |
| [uv](https://docs.astral.sh/uv/) | ✅ | Python and dependency management |

### Optional Tools

| Tool | Purpose |
|------|---------|
| [direnv](https://direnv.net) | Automatic virtual environment activation |
| [gh](https://github.com/cli/cli) | GitHub CLI for repository creation |

### Accounts (Optional but Recommended)
- **GitHub account** for repository hosting and CI/CD
- **PyPI account** for package publishing

## Step 1: Create Your Project

### Using uvx (Recommended)
```console
uvx cookiecutter gh:JnyJny/python-package-cookiecutter
```

### Using pip
```console
pip install cookiecutter
cookiecutter gh:JnyJny/python-package-cookiecutter
```

### Configuration Prompts

The template will ask you several questions to configure your project:

#### Basic Information
```
package_name [my_package]: your_package_name
package_description [A short description]: Your package description
author_name [Your Name]: Your Name
author_email [your.email@example.com]: your.email@example.com
github_username [yourusername]: yourusername
```

#### License Selection
```
license [MIT]:
  1 - MIT
  2 - Apache-2.0
  3 - GPL-3.0
  4 - BSD-3-Clause
  5 - no-license
```

#### Feature Options
```
use_pydantic_settings [True]: True/False
log_to_file [False]: True/False
create_github_repo [False]: True/False
build_backend [uv]: uv/hatch
```

#### Testing Configuration
```
python_testing_matrix [["3.11", "3.12", "3.13"]]: Python versions to test
os_testing_matrix [ubuntu-latest]: Operating systems to test
```

## Step 2: Navigate to Your Project

```console
cd your_package_name
```

Your project is now created with:
- ✅ Virtual environment created and activated
- ✅ Dependencies installed
- ✅ Git repository initialized
- ✅ Initial commit made
- ✅ (Optional) GitHub repository created

## Step 3: Explore Your Project

### View Available Tasks
```console
poe --help
```

You'll see tasks for:
- **Testing**: `poe test`, `poe coverage`
- **Code Quality**: `poe ty`, `poe ruff`, `poe check`, `poe qc`
- **Publishing**: `poe publish_patch`, `poe publish_minor`, `poe publish_major`
- **Documentation**: `poe docs-serve`, `poe docs-build`, `poe docs-deploy`
- **Utilities**: `poe clean`, `poe tree`

### Run Your CLI
```console
# Via python module
python -m your_package_name --help

# Or if installed in development mode
your_package_name --help
```

### Run Quality Checks
```console
poe qc
```

This runs:
- Type checking with `ty`
- Linting and formatting with `ruff`
- Tests with `pytest`
- Coverage reporting

## Step 4: Start Developing

### Edit Your Code
Your main code lives in:
- `src/your_package_name/__main__.py` - CLI entry point
- `src/your_package_name/__init__.py` - Package initialization
- `src/your_package_name/self_subcommand.py` - Built-in commands
- `src/your_package_name/settings.py` - Configuration (if enabled)

### Add Tests
Write tests in the `tests/` directory:
- `tests/test_cli.py` - CLI testing examples provided

### Update Documentation
- Edit `README.md` for your project description
- Add documentation in `docs/` directory
- Documentation auto-deploys to GitHub Pages

## Step 5: Publish Your Package

### Test Publishing (Optional)
```console
# Build your package
uv build

# Check the built package
ls dist/
```

### Publish to PyPI
```console
# For bug fixes
poe publish_patch

# For new features  
poe publish_minor

# For breaking changes
poe publish_major
```

This will:
1. ✅ Run all quality checks
2. ✅ Version your package
3. ✅ Create a git tag
4. ✅ Trigger GitHub Actions
5. ✅ Build and publish to PyPI
6. ✅ Create GitHub release
7. ✅ Deploy documentation

## Common Development Workflow

```console
# Make changes to your code
vim src/your_package_name/__main__.py

# Run quality checks
poe qc

# Run tests
poe test

# Commit your changes
git add .
git commit -m "Add new feature"

# When ready to release
poe publish_patch
```

## Next Steps

- **[Template User Guide](template-guide.md)** - Detailed feature documentation
- **[Customization Guide](customization.md)** - Modify your project
- **GitHub Workflows** - See template-guide.md for CI/CD pipeline details

## Troubleshooting

### Common Issues

**Virtual environment not activated?**
```console
source .venv/bin/activate  # Manual activation
# OR install direnv for automatic activation
```

**Tests failing?**
```console
poe test -v  # Verbose test output
```

**Build failing?**
```console
uv build --verbose  # Detailed build output
```

**GitHub Actions failing?**
- Check the Actions tab in your GitHub repository
- Ensure PyPI trusted publishing is configured (see template-guide.md)

### Getting Help

- **GitHub Issues**: Report bugs or ask questions
- **Documentation**: Check the complete template guide
- **Community**: Join discussions on GitHub