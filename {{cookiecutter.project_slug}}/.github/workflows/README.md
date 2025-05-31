# Publishing to PyPI

The release.yml workflow in this directory depends on you
having already setup a project on the [Python Package Index][pypi]
and [added a trusted publisher][trusted-publisher]. The workflow
depends on an environment named "pypi" which must agree with the
environment named when adding the trusted publisher. Additionally,
the project name on PyPI should match cookiecutter.project_slug
or modify release.yml to ensure the environment.url matches
the PyPI project URL.

## Testing

The release workflow has two stages:
- test
- publish

The test stage utilizes the `matrix` feature to test against a variety
of operating systems and python versions. This is likely more testing
than you might require, reduce the `os` and `python_versions` lists
to suit your needs.

The publish stage depends on all the tests finishing successfully
before continuing. The package will be built in a Linux container
and uses [uv][uv] for the build and published to PyPI on success.


[pypi]: https://pypi.org
[trusted-publisher]: https://docs.pypi.org/trusted-publishers/
[uv]: https://docs.astral.sh/uv/
