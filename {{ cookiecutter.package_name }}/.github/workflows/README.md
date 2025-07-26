# GitHub Actions Workflows

This directory contains GitHub Actions workflows for automated testing, building, publishing, and documentation deployment.

## Workflows Overview

### release.yaml - Test, Publish and Release

A comprehensive CI/CD pipeline with the following stages:
1. **get-python-versions** - Dynamically extract Python test versions from `pyproject.toml`
2. **test** - Run tests across multiple OS and Python versions
3. **build** - Build package artifacts
4. **publish** - Publish to PyPI
5. **github-release** - Create GitHub release with auto-generated changelog
6. **deploy-docs** - Trigger documentation deployment

### docs.yml - Deploy Documentation

Builds and deploys MkDocs documentation to GitHub Pages, triggered by:
- Repository dispatch events from release workflow
- Manual workflow dispatch

## Publishing to PyPI

The release workflow depends on you having already setup a project on the [Python Package Index][pypi] and [added a trusted publisher][trusted-publisher]. The workflow depends on an environment named "pypi" which must agree with the environment named when adding the trusted publisher. Additionally, the project name on PyPI should match `cookiecutter.package_name` or modify release.yaml to ensure `environment.url` matches the PyPI project URL.

## Testing Configuration

### Dynamic Python Version Detection

The workflow automatically detects Python test versions from your `pyproject.toml`:

```toml
[tool.{{ cookiecutter.package_name }}.ci]
test-python-versions = ["3.11", "3.12", "3.13"]
```

If not found, falls back to cookiecutter template defaults.

### Matrix Testing

The test stage utilizes the `matrix` feature to test against:
- Multiple operating systems (configurable via cookiecutter)
- Multiple Python versions (dynamic or fallback)

Reduce the `os` and `python_versions` lists in cookiecutter.json to suit your needs.

### Triggers

Tests are initiated when:
- A tag formatted as a [semantic version][semantic-version] is detected
- A tag with `-test` suffix is detected (for testing releases)
- Manual workflow dispatch

## Build and Deployment Process

1. **Testing**: All tests must pass before proceeding
2. **Build**: Package is built using [uv][uv] and artifacts are stored
3. **Publish**: Artifacts are published to PyPI using trusted publishing
4. **Release**: GitHub release is created with auto-generated changelog
5. **Documentation**: Docs deployment is triggered automatically

## Changelog and Release Notes

The workflow includes automatic changelog generation using:
- **BobAnkh/auto-generate-changelog** action for structured changelog updates
- **Git log analysis** for commit-based release notes
- **CHANGELOG.md integration** when available

## Documentation Deployment

The docs workflow:
- **Auto-enables GitHub Pages** if not already configured
- **Builds MkDocs documentation** with strict mode
- **Deploys to GitHub Pages** using artifact upload/download pattern
- **Triggered automatically** after successful releases via repository dispatch

## Tricksy Jinja Formatting

The release.yaml workflow uses some Jinja templating that needs to be
hidden from cookiecutter to ensure the proper rendering of the file.

For instance this line will cause cookiecutter to choke when
attempting to render the file:

{% raw %}
```yaml
  runs-on: ${{ matrix.os }}
```
{%- endraw %}

There are a couple of ways to fix this, I chose to enclose the
offending lines with Jinja `raw` and `endraw` tags as described
[here][jinja-whitespace-control].

Checkout [this post][jinja-tricks] for a great breakdown of all the
different ways this problem can be addressed.

<!-- End Links -->
[pypi]: https://pypi.org
[trusted-publisher]: https://docs.pypi.org/trusted-publishers/
[uv]: https://docs.astral.sh/uv/
[semantic-version]: https://semver.org
[jinja-tricks]: https://github.com/cookiecutter/cookiecutter/issues/1624#issuecomment-2031117503
[jinja-whitespace-control]: https://jinja.palletsprojects.com/en/stable/templates/#whitespace-control
