# Publishing to PyPI

The release.yml workflow in this directory depends on you having
already setup a project on the [Python Package Index][pypi] and [added
a trusted publisher][trusted-publisher]. The workflow depends on an
environment named "pypi" which must agree with the environment named
when adding the trusted publisher. It doesn't have to be named `pypi`
it just needs to match in both places. Additionally, the project name
on PyPI should match `cookiecutter.package_name` or modify release.yml
to ensure `environment.url` matches the PyPI project URL.

## Testing

The release workflow has two stages:
- test
- publish

The test stage utilizes the `matrix` feature to test against a variety
of operating systems and python versions. This is likely more testing
than you might require, reduce the `os` and `python_versions` lists
to suit your needs.

Tests are initiated when a tag formatted as a [semantic
version][semantic-version] is detected or with the suffix `-test` is
detected.

The publish stage depends on all the tests finishing successfully
before continuing. The package will be built in a Linux container
and uses [uv][uv] for the build and is published to PyPI on success.

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
