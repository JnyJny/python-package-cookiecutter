# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Cookiecutter template for creating Python packages with modern tooling. It generates opinionated Python projects with CLI interfaces, type checking, testing, and GitHub integration.

## Key Commands

### Testing the Template
- `pytest` - Run comprehensive test suite covering multiple aspects:
  - Template configuration validation (`test_cookiecutter_json.py`)
  - Project generation with all configuration combinations (`test_generate_projects.py`)
  - Generated project poe tasks functionality (`test_poe_tasks.py`)
  - CLI integration and behavior (`test_cli_integration.py`)
  - Build processes and packaging (`test_build_validation.py`)
  - Configuration matrix testing (`test_configuration_matrix.py`)
  - Cross-platform compatibility (`test_cross_platform.py`)
  - Edge cases and error handling (`test_edge_cases.py`)
  - End-to-end integration workflows (`test_integration.py`)
  - Default project baseline validation (`test_default_project.py`)
- `poe ruff` - Run ruff check and format on template code
- `poe test` - Run pytest (alias for pytest)

### Testing Generated Projects
- `poe bake` - Generate a test project in `./tmp/thing` using default values
- `poe clean` - Remove generated test project and GitHub repo

### Release Management
- `poe changelog` - Generate changelog since last tag
- `poe release-notes` - Generate release notes file from changelog
- `poe release_patch` - Bump patch version, commit, tag, and push (triggers GitHub release)
- `poe release_minor` - Bump minor version, commit, tag, and push (triggers GitHub release)
- `poe release_major` - Bump major version, commit, tag, and push (triggers GitHub release)

### Generated Project Commands
Generated projects include additional poe tasks:
- `poe changelog` - Generate changelog since last tag
- `poe release-notes` - Generate release notes file from changelog
- `poe publish_patch` - Publish patch release (triggers GitHub workflows)
- `poe publish_minor` - Publish minor release (triggers GitHub workflows)
- `poe publish_major` - Publish major release (triggers GitHub workflows)

### Development Setup
- `uv sync` - Install dependencies and sync virtual environment
- `uv run pytest` - Run tests with uv
- `uv run ruff check` - Run ruff checks

## Architecture

### Template Structure
- `cookiecutter.json` - Configuration with prompts and defaults for template generation
- `hooks/` - Pre/post generation scripts that run during cookiecutter execution
  - `pre_gen_project.uv` - Runs before template generation (currently no-op)
  - `post_gen_project.uv` - Runs after generation: installs Python, creates venv, syncs deps, initializes git, optionally creates GitHub repo
- `{{ cookiecutter.package_name }}/` - The actual template directory that gets rendered
- `tests/` - Tests for the cookiecutter template functionality

### Generated Project Structure
The template creates Python packages with:
- `src/` layout with package in `src/{{ cookiecutter.package_name }}/`
- Typer-based CLI with self-subcommands
- Optional pydantic-settings for configuration
- Loguru for logging
- Comprehensive poe tasks for development workflow
- Complete GitHub automation suite including:
  - CI/CD workflows for testing and PyPI publishing
  - Automatic GitHub release generation with changelogs
  - GitHub Pages documentation deployment
  - Dependabot for automated dependency updates
  - Issue and PR templates

### Hook System
Post-generation hooks automatically:
1. Install requested Python version with uv
2. Create virtual environment
3. Sync dependencies
4. Run ruff formatting
5. Initialize git repository
6. Create initial commit
7. Optionally create GitHub repository and push

### GitHub Automation Features

Generated projects include comprehensive GitHub automation:

**Workflows:**
- `release.yaml` - Multi-stage CI/CD pipeline with matrix testing and PyPI publishing via trusted publishers
- `github-release.yml` - Automatic GitHub release creation with changelog generation
- `docs.yml` - GitHub Pages deployment for MkDocs documentation
- `dependabot.yaml` - Automated dependency updates for Python packages and GitHub Actions

**Issue & PR Templates:**
- Bug report template with structured fields
- Feature request template
- Question template for support
- Pull request template with summary and test plan sections

**Release Management:**
- CHANGELOG.md following Keep a Changelog format
- Automated release notes generation from git commits
- Semantic versioning with tag-triggered releases
- Support for test releases with `-test` suffix tags

## Template Testing Strategy

The comprehensive test suite validates multiple aspects of the template:

### Template Configuration & Structure
- `cookiecutter.json` validation for proper structure and values
- File hierarchy generation across all configuration combinations
- Template rendering with different variable combinations

### Generated Project Functionality
- **Build & Packaging**: Wheel/sdist creation, installation, metadata validation
- **CLI Integration**: Help systems, error handling, version commands, debug functionality
- **Development Tools**: All poe tasks execution (test, lint, type-check, build)
- **Cross-Platform**: Path handling, line endings, permissions, Unicode support

### Workflow Integration
- **End-to-End Cycles**: Complete development workflows from test to build
- **Hook System**: Post-generation scripts (git init, venv creation, dependency sync)
- **GitHub Automation**: Workflow syntax validation, Dependabot configuration
- **Edge Cases**: Error conditions, boundary scenarios, invalid configurations

### Testing Infrastructure
- **Parametrized Testing**: Systematic coverage of configuration matrices
- **Subprocess Execution**: Real command behavior validation
- **File System Validation**: Structure and content verification
- **Performance Markers**: Separation of fast/slow tests for CI optimization

## Common Workflows

### Adding New Template Features
1. Modify template files in `{{ cookiecutter.package_name }}/`
2. Add corresponding tests in `tests/`
3. Test with `poe bake` and verify generated project works
4. Run `poe ruff` to ensure code quality

### Updating Dependencies
Update both:
- Root `pyproject.toml` for template development dependencies
- `{{ cookiecutter.package_name }}/pyproject.toml` for generated project dependencies

### Testing Generated Projects
The `poe bake` command creates a test project that can be used to verify template functionality without going through the full cookiecutter prompts.

### Working with GitHub Automation
When testing or modifying GitHub workflows:
1. Use `poe bake` to generate a test project with GitHub integration enabled
2. Test workflow changes in the generated project before updating the template
3. Verify Dependabot configuration with different `github_username` values
4. Test release workflows with semantic version tags (`v1.0.0`, `v1.0.0-test`)
5. Validate issue/PR templates render correctly with cookiecutter variables

### Release Process

**For the Cookiecutter Template Repository:**
1. Update code and commit changes
2. Run `poe changelog` to preview changes since last tag
3. Run `poe release-notes` to generate release notes
4. Use `poe release_patch/minor/major` to bump version, commit, tag, and push
5. GitHub Actions automatically create GitHub release with generated notes

**For Generated Projects:**
Generated projects follow this release workflow:
1. Update code and commit changes
2. Run `poe changelog` to preview changes since last tag (in generated project)
3. Run `poe release-notes` to generate release notes (in generated project)
4. Use `poe publish_patch/minor/major` to trigger automated release (in generated project)
5. GitHub Actions handle testing, PyPI publishing, and GitHub release creation