# Customization Guide

After creating your project with the cookiecutter template, you'll want to customize it 
to match your specific needs. This guide covers the most common modifications and 
customizations you should consider.

## Essential Customizations

### 1. Project Documentation

#### README.md
Your generated `README.md` contains template placeholders. Update these sections:

```markdown
# Your Package Name

**Update this description** to explain what your package does and why someone would use it.

## Installation

```bash
pip install your-package-name
```

## Usage

```python
import your_package

# Add real usage examples here
```

## Features

- List your actual features
- Remove template examples
- Add screenshots or demos if applicable
```

#### CONTRIBUTING.md
Update the contribution guidelines to reflect your project's needs:

- **Development setup**: Specific to your project
- **Code style**: Any additional style requirements
- **Testing requirements**: Coverage thresholds, test types
- **Review process**: How you handle pull requests

### 2. Package Configuration

#### pyproject.toml Updates

**Project Metadata**:
```toml
[project]
name = "your-package-name"
description = "Update with your actual description"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
keywords = ["add", "relevant", "keywords"]
classifiers = [
    # Update these PyPI classifiers
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12", 
    "Programming Language :: Python :: 3.13",
]
```

**Dependencies**:
```toml
dependencies = [
    # Add your actual runtime dependencies
    "requests>=2.28.0",
    "pydantic>=2.0.0",
    # Remove template dependencies you don't need
]

[dependency-groups]
dev = [
    # Add development dependencies specific to your project
    "pytest-asyncio",  # If you use async code
    "httpx",          # For HTTP testing
    # Keep the quality tools unless you prefer alternatives
]
```

#### Testing Configuration
```toml
[tool.pytest.ini_options]
# Add markers specific to your project
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
]

# Add test paths specific to your project
testpaths = ["tests"]
# Configure coverage
addopts = "--cov=src/your_package --cov-report=html --cov-report=term-missing"
```

### 3. Code Quality Configuration

#### Ruff Configuration
Customize linting rules in `pyproject.toml`:

```toml
[tool.ruff]
# Adjust line length if needed
line-length = 88

[tool.ruff.lint]
# Add or remove rule categories
select = ["ALL"]
ignore = [
    # Add rules you want to ignore
    "D203",    # 1 blank line required before class docstring
    "D213",    # Multi-line docstring summary should start at the second line
    # Add project-specific ignores
]

[tool.ruff.lint.per-file-ignores]
# Different rules for different file types
"tests/*" = ["S101", "PLR2004"]  # Allow assert and magic values in tests
"scripts/*" = ["T201"]           # Allow print in scripts
```

#### Type Checking with ty
Configure ty for your project needs:

```toml
[tool.ty]
# Add specific configuration for ty if needed
```

### 4. GitHub Workflows Customization

#### Modify Python Version Matrix
Edit your project's `pyproject.toml`:

```toml
[tool.your_package.ci]
test-python-versions = ["3.11", "3.12", "3.13"]  # Adjust as needed
```

#### Operating System Matrix
Modify `.github/workflows/release.yaml` if you need different OS coverage:

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]  # Adjust as needed
```

#### Environment Variables
Add project-specific environment variables to workflows:

```yaml
env:
  YOUR_API_KEY: ${{ secrets.YOUR_API_KEY }}
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

### 5. Documentation Customization

#### MkDocs Configuration
Edit `mkdocs.yml` to customize your documentation:

```yaml
site_name: Your Package Documentation
site_description: Detailed description of your package

# Add custom navigation
nav:
  - Home: index.md
  - Getting Started:
    - Installation: getting-started/installation.md
    - Quick Start: getting-started/quickstart.md
    - Configuration: getting-started/configuration.md
  - User Guide:
    - CLI Usage: user-guide/cli.md
    - API Reference: user-guide/api.md
    - Examples: user-guide/examples.md
  - Contributing: contributing.md
  - Changelog: changelog.md

# Customize theme
theme:
  name: material  # or your chosen theme
  palette:
    - scheme: default
      primary: blue
      accent: blue
```

#### Add Custom Documentation Pages
Create documentation specific to your project:

```markdown
# docs/user-guide/api.md
# API Reference

## Core Functions

### your_function()
Description of your main function...

## Classes

### YourClass
Description of your main class...
```

## Advanced Customizations

### 1. Custom CLI Commands

Extend the CLI in `src/your_package/__main__.py`:

```python
import typer
from your_package.commands import data_command, export_command

app = typer.Typer(
    name="your_package",
    help="Your package description and main help text.",
)

# Add your custom commands
app.add_typer(data_command.app, name="data", help="Data management commands")
app.add_typer(export_command.app, name="export", help="Export commands")

@app.command()
def process(
    input_file: Path = typer.Argument(..., help="Input file to process"),
    output_file: Path = typer.Option(None, help="Output file path"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
):
    """Process an input file and generate output."""
    # Your command implementation
    pass
```

### 2. Configuration Management

Extend settings in `src/your_package/settings.py`:

```python
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database settings
    database_url: str = "sqlite:///app.db"
    database_echo: bool = False
    
    # API settings
    api_key: Optional[str] = None
    api_timeout: int = 30
    
    # Logging settings
    log_level: str = "INFO"
    log_file: Optional[str] = None
    
    # Feature flags
    enable_feature_x: bool = False
    
    class Config:
        env_prefix = "YOUR_PACKAGE_"
        env_file = ".env"
```

### 3. Custom Poe Tasks

Add project-specific tasks to `pyproject.toml`:

```toml
[tool.poe.tasks]
# Data management tasks
migrate = "alembic upgrade head"
seed-data = "python scripts/seed_database.py"
backup = "python scripts/backup.py"

# Custom quality tasks
lint-docs = "ruff check docs/"
check-security = "bandit -r src/"
validate-schema = "python scripts/validate_schema.py"

# Deployment tasks
deploy-staging = "python scripts/deploy.py --env staging"
deploy-prod = "python scripts/deploy.py --env production"

# Custom sequences
full-check.sequence = ["ruff", "ty", "test", "check-security"]
deploy-pipeline.sequence = ["full-check", "build", "deploy-staging"]
```

### 4. Testing Strategy

#### Custom Test Configuration
Add test utilities in `tests/conftest.py`:

```python
import pytest
from your_package import create_app
from your_package.database import get_db

@pytest.fixture
def app():
    """Create application for testing."""
    return create_app(testing=True)

@pytest.fixture
def db():
    """Create database for testing."""
    # Setup test database
    yield get_db()
    # Cleanup

@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {
        "users": [...],
        "products": [...],
    }
```

#### Test Categories
Organize tests with markers:

```python
# tests/test_integration.py
import pytest

@pytest.mark.integration
def test_database_connection():
    """Test database connectivity."""
    pass

@pytest.mark.slow
def test_large_data_processing():
    """Test processing large datasets."""
    pass
```

Run specific test categories:
```console
poe test -m "not slow"        # Skip slow tests
poe test -m integration       # Only integration tests
poe test -m "unit and not slow"  # Unit tests that are fast
```

## Project-Specific Modifications

### 1. Remove Unused Features

If you don't need certain template features:

#### Remove Pydantic Settings
1. Delete `src/your_package/settings.py`
2. Remove pydantic-settings from dependencies
3. Update `__main__.py` to remove settings imports

#### Remove File Logging
1. Remove file logging configuration from `__main__.py`
2. Update loguru configuration to console-only

#### Simplify CLI
If you only need a simple CLI:
1. Remove complex command structure
2. Simplify `__main__.py` to basic argument parsing
3. Remove unnecessary CLI dependencies

### 2. Add Domain-Specific Features

#### Web API with FastAPI
Add FastAPI for web APIs:

```python
# src/your_package/api.py
from fastapi import FastAPI
from your_package.routes import items_router

app = FastAPI(title="Your Package API")
app.include_router(items_router, prefix="/api/v1")
```

#### Database Integration
Add database support:

```python
# src/your_package/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

#### Background Tasks
Add task queue integration:

```python
# src/your_package/tasks.py
from celery import Celery

celery_app = Celery("your_package")

@celery_app.task
def process_data(data_id: str):
    """Process data in background."""
    pass
```

## Deployment Customizations

### 1. Docker Support
Add Docker configuration:

```dockerfile
# Dockerfile
FROM python:3.13-slim

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen

COPY src/ ./src/
RUN uv pip install -e .

CMD ["your-package"]
```

### 2. Environment Configuration
Add environment-specific configuration:

```python
# src/your_package/config.py
import os
from enum import Enum

class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"  
    PRODUCTION = "production"

def get_settings():
    env = os.getenv("ENVIRONMENT", Environment.DEVELOPMENT)
    
    if env == Environment.PRODUCTION:
        return ProductionSettings()
    elif env == Environment.STAGING:
        return StagingSettings()
    else:
        return DevelopmentSettings()
```

### 3. CI/CD Enhancements
Add deployment steps to `.github/workflows/release.yaml`:

```yaml
deploy:
  needs: [publish, github-release]
  if: success()
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - name: Deploy to production
      run: |
        # Your deployment commands
        echo "Deploying to production..."
```

## Maintenance Tasks

### Regular Updates
1. **Dependencies**: Review and update dependencies quarterly
2. **Python versions**: Add new Python versions as they're released
3. **GitHub Actions**: Update action versions annually
4. **Documentation**: Keep documentation current with code changes

### Quality Monitoring
1. **Test coverage**: Maintain >90% test coverage
2. **Security**: Run security scans regularly
3. **Performance**: Monitor package size and import time
4. **Dependencies**: Monitor for security vulnerabilities

This customization guide should help you adapt the template to your specific needs while maintaining the quality and automation features that make it valuable.