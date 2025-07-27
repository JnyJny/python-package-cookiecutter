# Contributing to python-package-cookiecutter

We have issues labeled as [Good First Issue][good-first-issue] and
[Help Wanted][help-wanted] which are good opportunities for new
contributors.

Thank you for your contributions to this project!


## Prequisites Tools

| Tool | Purpose |
|------|---------|
|[uv][uv] | manage python, virtual environments and package building |
|[direnv][direnv] | automatic virtual environment activation |
|[gh][gh] | manage GitHub repos from the command line |


## Setup

```console
git clone https://github.com/JnyJny/python-package-cookiecutter
cd python-package-cookiecutter
uv sync --all-groups
```

## Testing the Cookiecutter Template

```console
poe ruff
pytest
```

## Testing the Generated Project

```console
poe bake
pushd tmp/thing
pytest
popd
poe clean
```

## Documentation

Documentation is built using [MkDocs](https://www.mkdocs.org/) with
the Material theme and deployed to GitHub Pages.

### Local Development

```console
# Serve docs locally with live reload
poe docs-serve

# Build docs for production
poe docs-build

# Deploy docs to GitHub Pages (maintainers only)
poe docs-deploy
```

### Documentation Structure

- `docs/index.md` - Main documentation hub with navigation
- `docs/overview.md` - Template features and benefits
- `docs/quickstart.md` - Getting started guide
- `docs/template-guide.md` - Detailed feature documentation
- `docs/customization.md` - Post-creation modification guide
- `mkdocs.yml` - MkDocs configuration

### Writing Guidelines

- Keep markdown lines under 90 columns
- Use end links format instead of embedded URLs
- Include code examples where helpful
- Cross-reference related sections
- Test all code examples before committing

### Documentation Deployment

Documentation auto-deploys to GitHub Pages when:
1. Changes are merged to `main` branch
2. A new release is created

The deployment workflow builds the docs and publishes them to the `gh-pages` branch.

## Releases

### Pre-Release Activities

1. `poe ruff` reports no changes
1. `pytest` reports no failures
1. `poe bake; pushd tmp/thing; pytest` reports no failures
1. `poe bake; pushd tmp/thing; poe ruff` reports no changes
1. Commit your changes and create a pull request.

### Releasing

- `poe release_major` - New features, breaking changes
- `poe release_minor` - New features, non-breaking changes
- `poe release_patch` - bug fixes

<!-- End Links -->

[good-first-issue]: https://github.com/JnyJny/python-project-cookiecutter/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22
[help-wanted]: https://github.com/github.com/JnyJny/python-project-cookiecutter/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22

[uv]: https://docs.astral.sh/uv/
[direnv]: https://direnv.net
[gh]: https://github.com/cli/cli
