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
uv sync
```

## Testing the Cookiecutter Template

```console
pytest
poe ruff
```

## Testing the Generated Project

```console
poe bake
pushd tmp/thing
pytest
poe ruff
popd
poe clean
```

## Documentation

_TBD_

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
