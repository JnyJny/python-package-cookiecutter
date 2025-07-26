# Changelog

All notable changes to {{ cookiecutter.project_name }} will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of {{ cookiecutter.project_name }}
- Command-line interface with Typer
- Structured logging with Loguru
{% if cookiecutter.use_pydantic_settings -%}
- Configuration management with Pydantic Settings
{% endif -%}
- Type checking with ty
- Code quality tools (ruff, pytest)
- Comprehensive documentation with MkDocs

### Changed
- Nothing yet

### Deprecated
- Nothing yet

### Removed
- Nothing yet

### Fixed
- Nothing yet

### Security
- Nothing yet

## [{{ cookiecutter.project_version }}] - {% now 'utc', '%Y-%m-%d' %}

### Added
- Initial release

[Unreleased]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/compare/v{{ cookiecutter.project_version }}...HEAD
[{{ cookiecutter.project_version }}]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/releases/tag/v{{ cookiecutter.project_version }}