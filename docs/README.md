# Documentation

This directory contains comprehensive documentation for the Python Package Cookiecutter Template.

## Documentation Structure

- **[index.md](index.md)** - Main documentation hub with navigation
- **[overview.md](overview.md)** - Template overview and value proposition
- **[quickstart.md](quickstart.md)** - Get started in minutes
- **[template-guide.md](template-guide.md)** - Detailed feature documentation
- **[customization.md](customization.md)** - How to modify generated projects

## Building Documentation

This documentation is written in Markdown and can be used with various documentation generators:

### With MkDocs
```bash
# Install MkDocs
pip install mkdocs mkdocs-material

# Create mkdocs.yml (see example below)
# Serve locally
mkdocs serve

# Build for deployment
mkdocs build
```

### With Sphinx
```bash
# Install Sphinx
pip install sphinx sphinx-rtd-theme myst-parser

# Configure Sphinx to use Markdown
# Build documentation
sphinx-build -b html docs/ docs/_build/
```

### Example mkdocs.yml
```yaml
site_name: Python Package Cookiecutter Template
docs_dir: docs
site_dir: site

nav:
  - Home: index.md
  - Overview: overview.md
  - Quick Start: quickstart.md
  - Template Guide: template-guide.md
  - Customization: customization.md

theme:
  name: material
  palette:
    - scheme: default
      primary: blue
      accent: blue

markdown_extensions:
  - admonition
  - codehilite
  - toc:
      permalink: true
```

## Contributing to Documentation

When contributing to the documentation:

1. **Keep lines under 90 characters** for readability
2. **Use clear headings** with consistent hierarchy
3. **Include code examples** where helpful
4. **Link between documents** to improve navigation
5. **Test documentation builds** before submitting

## Viewing Documentation

The documentation can be viewed:
- **Locally**: Using MkDocs serve or Sphinx build
- **GitHub**: Markdown files render directly in the repository
- **GitHub Pages**: When deployed with MkDocs or Sphinx