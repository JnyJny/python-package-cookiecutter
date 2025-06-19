"""python-package-cookiecutter testing fixtures."""

import pytest
from pathlib import Path
import json

from cookiecutter.main import cookiecutter as bake

_PROJECT = "python-package-cookiecutter"


@pytest.fixture(scope="session")
def template_root() -> Path:
    """The path for the template under test."""

    # EJO is there a better way to do this? Probably.

    p, root = Path.cwd(), Path("/")

    while p != root:
        if p.name == _PROJECT:
            break
        p = p.parent
    else:
        raise RuntimeError(f"Could not find the {_PROJECT} root directory.")
    yield p


@pytest.fixture(scope="session")
def cookiecutter_json_path(template_root) -> Path:
    """Path to the cookiecutter.json file."""

    yield template_root / "cookiecutter.json"


@pytest.fixture(scope="session")
def cookiecutter_json_contents(cookiecutter_json_path: Path) -> dict:
    """Dictionary of data derived from cookiecutter.json."""
    yield json.load(cookiecutter_json_path.open())


@pytest.fixture(scope="session")
def cookiecutter_extra_context() -> dict:
    return {"create_github_repo": False}


@pytest.fixture(scope="session")
def cookiecutter_package_name(cookiecutter_json_contents) -> str:
    yield cookiecutter_json_contents["package_name"]


@pytest.fixture(scope="session")
def generated_template_path(
    tmp_path_factory,
    template_root,
    cookiecutter_package_name,
    cookiecutter_extra_context,
) -> Path:
    """Returns a path to the generated project in a temporary directory."""
    tmp_path = tmp_path_factory.mktemp("template_output")
    bake(
        template=str(template_root),
        no_input=True,
        extra_context=cookiecutter_extra_context,
        output_dir=tmp_path,
    )
    yield tmp_path / cookiecutter_package_name
