# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure
- CLI interface with Typer
- Basic logging with Loguru
{% if cookiecutter.use_pydantic_settings -%}
- Configuration management with Pydantic Settings
{% endif -%}
- MkDocs documentation with {{ cookiecutter.mkdocs_theme }} theme
- GitHub Actions for testing and publishing
- Automatic GitHub release generation

### Changed

### Deprecated

### Removed

### Fixed

### Security

## [{{ cookiecutter.project_version }}] - {{ cookiecutter.year }}-01-01

### Added
- Initial release of {{ cookiecutter.project_name }}