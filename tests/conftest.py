"""python-package-cookiecutter testing fixtures."""

import json
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter as bake

_PROJECT = "python-package-cookiecutter"


@pytest.fixture(scope="session")
def template_root() -> Path:
    """Return the path for the template under test."""
    # EJO is there a better way to do this? Probably.

    p, root = Path.cwd(), Path("/")

    while p != root:
        if p.name == _PROJECT:
            break
        p = p.parent
    else:
        msg = f"Could not find the {_PROJECT} root directory."
        raise RuntimeError(msg)
    return p


@pytest.fixture(scope="session")
def cookiecutter_json_path(template_root: Path) -> Path:
    """Return Path to the cookiecutter.json file."""
    return template_root / "cookiecutter.json"


@pytest.fixture(scope="session")
def cookiecutter_json_contents(cookiecutter_json_path: Path) -> dict:
    """Return dictionary of data derived from cookiecutter.json."""
    return json.load(cookiecutter_json_path.open())


@pytest.fixture(scope="session")
def cookiecutter_extra_context() -> dict:
    """Return a dictionary disabling create_github_repo action."""
    return {"create_github_repo": False}


@pytest.fixture(scope="session")
def cookiecutter_package_name(cookiecutter_json_contents: dict) -> str:
    """Return the cookiecutter.package_name."""
    return cookiecutter_json_contents["package_name"]


@pytest.fixture(scope="session")
def generated_template_path(
    tmp_path_factory: pytest.TempPathFactory,
    template_root: Path,
    cookiecutter_package_name: str,
    cookiecutter_extra_context: dict,
) -> Path:
    """Return a path to the generated project in a temporary directory."""
    tmp_path = tmp_path_factory.mktemp("template_output")
    bake(
        template=str(template_root),
        no_input=True,
        extra_context=cookiecutter_extra_context,
        output_dir=tmp_path,
    )
    return tmp_path / cookiecutter_package_name
