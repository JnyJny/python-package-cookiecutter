# Template User Guide

This guide provides detailed information about all features available in the Python Package Cookiecutter Template and how to use them effectively.

## Template Features

### Project Structure

The template creates a well-organized project following Python packaging best practices:

```
your-package/
├── .cookiecutter.json      # Template configuration used
├── .envrc                  # direnv configuration (optional)
├── .github/                # GitHub workflows and templates
│   ├── workflows/
│   │   ├── release.yaml    # CI/CD pipeline
│   │   └── docs.yml        # Documentation deployment
│   ├── ISSUE_TEMPLATE/     # GitHub issue templates
│   │   ├── 1_bug_report.yaml
│   │   ├── 2_feature_request.yaml
│   │   ├── 3_question.yaml
│   │   └── config.yaml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── dependabot.yaml     # Dependency updates
├── .gitignore              # Comprehensive gitignore
├── CONTRIBUTING.md         # Contribution guidelines
├── docs/                   # MkDocs documentation
│   ├── index.md
│   ├── getting-started/
│   ├── user-guide/
│   ├── changelog.md
│   ├── contributing.md
│   └── gen_ref_pages.py    # Auto-generates API docs
├── LICENSE                 # Your chosen license
├── mkdocs.yml              # Documentation configuration
├── pyproject.toml          # Project and tool configuration
├── README.md               # Project documentation
├── src/                    # Source code (src layout)
│   └── your_package/
│       ├── __init__.py
│       ├── __main__.py     # CLI entry point
│       ├── self_subcommand.py  # Built-in commands
│       └── settings.py     # Configuration (optional)
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── conftest.py
│   └── test_cli.py
└── uv.lock                 # Dependency lock file
```

### Core Components

#### Command Line Interface (CLI)
Every package includes a fully functional CLI built with Typer:

- **Main CLI**: Accessible via `python -m your_package` or `your_package`
- **Built-in Commands**: Version, help, and self-diagnostics
- **Extensible**: Easy to add new commands and subcommands
- **Rich Output**: Beautiful help text and error messages

#### Configuration Management
Optional Pydantic Settings integration:

```python
# src/your_package/settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    debug: bool = False
    log_level: str = "INFO"
    
    class Config:
        env_prefix = "YOUR_PACKAGE_"
```

Usage:
```console
export YOUR_PACKAGE_DEBUG=true
export YOUR_PACKAGE_LOG_LEVEL=DEBUG
your_package command
```

#### Logging
Loguru-based logging with optional file output:

```python
from loguru import logger

logger.info("Application started")
logger.debug("Debug information")
logger.error("Something went wrong")
```

With file logging enabled:
- Console output for development
- Rotating log files for production
- Structured logging with timestamps

### Development Tools

#### Poe The Poet Tasks
Pre-configured tasks in `pyproject.toml`:

```console
# Code Quality
poe ty              # Type checking with ty
poe ruff-check      # Linting with ruff
poe ruff-format     # Code formatting with ruff
poe ruff            # Both linting and formatting
poe check           # Quick quality checks
poe qc              # Comprehensive quality control

# Testing
poe test            # Run pytest
poe coverage        # Generate coverage report

# Publishing
poe publish_patch   # Patch version release (1.0.0 -> 1.0.1)
poe publish_minor   # Minor version release (1.0.0 -> 1.1.0)
poe publish_major   # Major version release (1.0.0 -> 2.0.0)
poe publish         # Alias for publish_minor

# Documentation
poe docs-serve      # Serve docs locally
poe docs-build      # Build documentation
poe docs-deploy     # Deploy to GitHub Pages

# Utilities
poe clean           # Remove build artifacts
poe tree            # Show project structure
```

#### Quality Assurance
Comprehensive code quality tools:

- **Ruff**: Lightning-fast linting and formatting
- **ty**: Type checking for Python
- **pytest**: Testing framework with fixtures
- **Coverage**: Code coverage reporting

### GitHub Integration

#### Workflows
Two main GitHub Actions workflows:

**Release Workflow** (`release.yaml`):
1. **Dynamic Python Version Detection**: Reads test versions from `pyproject.toml`
2. **Matrix Testing**: Tests across Python versions and operating systems
3. **Build Package**: Creates wheel and source distributions
4. **Publish to PyPI**: Uses trusted publishing (no API tokens)
5. **GitHub Release**: Auto-generates release notes and changelog
6. **Deploy Documentation**: Triggers documentation deployment

**Documentation Workflow** (`docs.yml`):
1. **Auto-enable GitHub Pages**: Sets up Pages if not already configured
2. **Build Documentation**: Compiles MkDocs site
3. **Deploy**: Publishes to GitHub Pages

#### Issue Templates
Professional GitHub issue templates:

- **Bug Report**: Structured bug reporting with environment details
- **Feature Request**: Template for suggesting new features
- **Question**: General questions and discussion
- **Configuration**: Links to discussions and documentation

#### Dependabot
Automatic dependency updates:
- **Python dependencies**: Daily checks
- **GitHub Actions**: Weekly checks
- **Grouped updates**: Related dependencies updated together

### Documentation System

#### MkDocs Integration
Complete documentation setup with theme options:

**Available Themes**:
- **Material**: Feature-rich with dark/light mode
- **Read the Docs**: Classic documentation style
- **MkDocs**: Default lightweight theme
- **Bootstrap**: Responsive design
- **Windmill**: Clean minimal theme

**Features**:
- **Auto-generated API documentation** from docstrings
- **Search functionality** with highlighting
- **Automatic deployment** to GitHub Pages
- **Navigation structure** with user guide and examples

#### Documentation Structure
```
docs/
├── index.md                # Homepage
├── getting-started/
│   ├── installation.md     # Installation instructions
│   ├── quickstart.md       # Quick start guide
│   └── configuration.md    # Configuration options
├── user-guide/
│   ├── cli.md             # CLI usage
│   └── examples.md        # Usage examples
├── contributing.md        # Contribution guidelines
└── changelog.md           # Project changelog
```

## Configuration Options

### Cookiecutter Variables

#### Basic Project Information
```json
{
    "package_name": "my_package",
    "package_description": "A short description of the package",
    "author_name": "Your Name", 
    "author_email": "your.email@example.com",
    "github_username": "yourusername",
    "project_version": "0.1.0"
}
```

#### License Options
```json
{
    "license": [
        "MIT",
        "Apache-2.0", 
        "GPL-3.0",
        "BSD-2-Clause",
        "BSD-3-Clause",
        "BSL-1.0",
        "CC0-1.0",
        "EPL-2.0",
        "GPL-2.0",
        "LGPL-2.1",
        "MPL-2.0",
        "AGPL-3.0",
        "no-license"
    ]
}
```

#### Feature Toggles
```json
{
    "use_pydantic_settings": true,
    "log_to_file": false,
    "create_github_repo": false,
    "make_github_repo_private": false,
    "readme_badges": true
}
```

#### Build and CI Configuration
```json
{
    "build_backend": ["uv", "hatch"],
    "python_version_dev": "3.13",
    "python_testing_matrix": ["3.11", "3.12", "3.13"],
    "os_testing_matrix": "ubuntu-latest, macos-latest, windows-latest"
}
```

#### Documentation Options
```json
{
    "mkdocs_theme": [
        "material",
        "readthedocs", 
        "mkdocs",
        "bootstrap",
        "windmill"
    ]
}
```

### Advanced Configuration

#### CI/CD Customization
Modify Python versions and OS matrix in your project's `pyproject.toml`:

```toml
[tool.your_package.ci]
test-python-versions = ["3.11", "3.12", "3.13"]
```

The workflow automatically detects and uses these versions.

#### Build Backend Selection
Choose between build backends:

- **uv** (default): Fast, modern dependency resolution
- **hatch**: Traditional, well-established build system

## GitHub Actions Workflow Details

### Workflow Triggers
The release workflow triggers on:
- **Semantic version tags**: `v1.0.0`, `v2.1.3`, etc.
- **Pull requests**: Runs tests only
- **Manual dispatch**: For testing

### Workflow Jobs

#### 1. Get Python Versions
- Extracts Python test versions from `pyproject.toml`
- Falls back to default versions if not specified
- Outputs versions for matrix testing

#### 2. Test Matrix
- Tests across Python versions and operating systems
- Runs comprehensive test suite
- Checks code quality with ruff and ty

#### 3. Build Package
- Creates wheel and source distributions
- Uploads artifacts for other jobs
- Only runs on successful tests and version tags

#### 4. Publish to PyPI
- Uses PyPI trusted publishing (no API tokens needed)
- Downloads build artifacts
- Publishes to PyPI automatically

#### 5. GitHub Release
- Auto-generates changelog from git history
- Creates GitHub release with notes
- Attaches build artifacts
- Only runs on successful publishing

#### 6. Deploy Documentation
- Triggers documentation workflow via repository dispatch
- Ensures documentation updates after releases

### Trusted Publishing Setup
For PyPI publishing to work, configure trusted publishing:

1. **Go to PyPI**: https://pypi.org/manage/account/publishing/
2. **Add a new trusted publisher**:
   - Repository name: `your-username/your-package`
   - Workflow name: `release.yaml`
   - Environment name: `pypi` (optional but recommended)

## Next Steps

- **[Customization Guide](customization.md)** - How to modify your generated project
- **[Advanced Features](advanced.md)** - Power user features and tips
- **[Contributing](../CONTRIBUTING.md)** - Contributing to the template itself