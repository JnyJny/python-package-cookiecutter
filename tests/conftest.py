"""python-package-cookiecutter testing fixtures."""

import json
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter as bake

_PROJECT = "python-package-cookiecutter"

# EJO This file manifest is super fragile, it should be generated from
#     template data rather than duplicated here. It's a start.

MANIFEST = [
    ("is_dir", ".git"),
    ("is_dir", ".github"),
    ("is_dir", ".github/ISSUE_TEMPLATE"),
    ("is_dir", ".github/workflows"),
    ("is_dir", ".venv"),
    ("is_dir", "src"),
    ("is_dir", "tests"),
    ("is_file", ".envrc"),
    ("is_file", ".github/ISSUE_TEMPLATE/1_bug_report.yaml"),
    ("is_file", ".github/ISSUE_TEMPLATE/2_feature_request.yaml"),
    ("is_file", ".github/ISSUE_TEMPLATE/3_question.yaml"),
    ("is_file", ".github/ISSUE_TEMPLATE/config.yaml"),
    ("is_file", ".github/PULL_REQUEST_TEMPLATE.md"),
    ("is_file", ".github/dependabot.yaml"),
    ("is_file", ".github/workflows/README.md"),
    ("is_file", ".github/workflows/release.yaml"),
    ("is_file", ".gitignore"),
    ("is_file", "LICENSE"),
    ("is_file", "README.md"),
    ("is_file", "pyproject.toml"),
    ("is_file", "uv.lock"),
]

SRC = ["__init__.py", "__main__.py", "self_subcommand.py", "settings.py"]


def check_project_contents(
    project_path: Path | str,
    project_name: str,
) -> bool:
    """Check that the project contents match the expected manifest."""
    project_path = Path(project_path)

    assert project_path.exists()
    assert project_path.is_dir()

    for content_test, content_path in MANIFEST:
        path = project_path / content_path

        assert path.exists(), f"Expected {path} to exist"
        assert getattr(path, content_test)(), f"Expected {content_test} for {path}"

        if path.is_file():
            assert path.stat().st_size > 0, f"File {path} is unexpectedly empty"

    src = project_path / "src" / project_name
    for path in src.rglob("*.py"):
        assert path.name in SRC

    return True


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
