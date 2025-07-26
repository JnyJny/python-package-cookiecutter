# GitHub Actions Workflows for Template Repository

This directory contains GitHub Actions workflows for the cookiecutter template repository itself.

## Workflows

### release.yaml - Test and Release Template

A CI/CD pipeline for the cookiecutter template repository with the following stages:

1. **test** - Run template tests across multiple Python versions
2. **github-release** - Create GitHub releases with auto-generated changelogs

### Triggers

- **Pull Requests**: Runs tests on all PRs to main branch
- **Push to main**: Runs tests on main branch pushes  
- **Tags**: Creates GitHub releases for semantic version tags (v1.0.0, v1.2.3, etc.)
- **Manual**: Can be triggered manually via workflow_dispatch

### Testing

The workflow runs the fast test suite (`poe test_fast`) across Python 3.11, 3.12, and 3.13 to validate that the template generates correctly and all basic functionality works.

### Release Process

When a semantic version tag is pushed (e.g., `v1.0.0`):

1. **Auto-changelog Generation**: Uses BobAnkh/auto-generate-changelog to update CHANGELOG.md
2. **Release Notes**: Generates commit-based release notes since the last tag
3. **GitHub Release**: Creates a GitHub release with the generated notes

### Usage

To create a release:

```bash
# Create and push a semantic version tag
git tag v1.0.0
git push origin v1.0.0
```

The workflow will automatically:
- Run tests to ensure template quality
- Update the CHANGELOG.md file
- Create a GitHub release with release notes
- Commit the changelog updates back to the repository

### No PyPI Publishing

This workflow is specifically designed for the cookiecutter template repository and does **not** publish to PyPI, since the template itself is not a Python package but rather a project generator.