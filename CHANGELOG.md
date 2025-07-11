# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Automatic changelog and GitHub release generation for cookiecutter repo
- CHANGELOG.md following Keep a Changelog format
- Enhanced poe tasks for release management
- GitHub Actions workflow for automatic releases

### Changed

### Deprecated

### Removed

### Fixed

### Security

## [1.7.2] - 2025-07-09

### Changed
- Updated test_cli_integration
- Pruned out some tests that were over-the-top

## [1.7.1] - 2025-07-09

### Added
- GitHub Actions workflow for automatic release creation
- Release notes generation with changelog
- CHANGELOG.md template for generated projects
- Updated README with release management documentation
- Poe tasks for changelog and release notes generation in generated projects

### Changed
- Updated post_gen_project.uv
- Updated dependabot.yml

## [1.7.0] - 2025-07-09

### Added
- Dependabot configuration for automated dependency updates
- Python dependencies checked daily at 8:00 AM CT
- GitHub Actions checked weekly on Mondays at 8:00 AM CT
- PR limits, commit message prefixes, and reviewers configuration
- Appropriate labels for dependency type classification
- Comprehensive automated dependency management for both main repository and generated projects

### Changed
- Updated project release.yml

## [1.6.x and earlier]

### Added
- Initial cookiecutter template for Python packages
- Modern tooling integration (uv, ruff, mypy, pytest)
- Typer-based CLI interface
- Optional pydantic-settings for configuration
- Loguru for logging
- Comprehensive poe tasks for development workflow
- GitHub workflows for testing and publishing
- MkDocs documentation with multiple theme options
- Cross-platform compatibility
- Comprehensive test suite