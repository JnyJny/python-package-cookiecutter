# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Cookiecutter template for creating Python packages with modern tooling. It generates opinionated Python projects with CLI interfaces, type checking, testing, and GitHub integration.

## Key Commands

### Testing the Template
- `pytest` - Run tests for the cookiecutter template itself
- `poe ruff` - Run ruff check and format on template code
- `poe test` - Run pytest (alias for pytest)

### Testing Generated Projects
- `poe bake` - Generate a test project in `./tmp/thing` using default values
- `poe clean` - Remove generated test project and GitHub repo

### Release Management
- `poe release_patch` - Bump patch version, commit, tag, and push
- `poe release_minor` - Bump minor version, commit, tag, and push  
- `poe release_major` - Bump major version, commit, tag, and push

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
- GitHub workflows for testing and publishing

### Hook System
Post-generation hooks automatically:
1. Install requested Python version with uv
2. Create virtual environment
3. Sync dependencies
4. Run ruff formatting
5. Initialize git repository
6. Create initial commit
7. Optionally create GitHub repository and push

## Template Testing Strategy

Tests validate the template by:
- Checking cookiecutter.json structure and values
- Generating projects with various configuration combinations
- Running tests within generated projects
- Verifying all poe tasks work in generated projects

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