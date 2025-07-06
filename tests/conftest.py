"""python-package-cookiecutter testing fixtures."""

import json
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter as bake

_PROJECT = "python-package-cookiecutter"

# Base manifest that all projects should have
BASE_MANIFEST = [
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
    ("is_file", "README.md"),
    ("is_file", "pyproject.toml"),
    ("is_file", "uv.lock"),
]

BASE_SRC = ["__init__.py", "__main__.py", "self_subcommand.py"]


def generate_expected_manifest(cookiecutter_context: dict) -> list[tuple[str, str]]:
    """Generate expected file manifest based on cookiecutter context."""
    manifest = []
    
    # Files created by hooks
    hook_files = {".git", ".venv", "uv.lock"}
    
    # Add base files that don't depend on hooks
    for test_type, path in BASE_MANIFEST:
        if path not in hook_files:
            manifest.append((test_type, path))
    
    # LICENSE file is always included (even for no-license, it's an Unlicense)
    manifest.append(("is_file", "LICENSE"))
    
    # Add files created by hooks if we expect them to have run
    if cookiecutter_context.get("_hooks_ran", True):
        manifest.extend([
            ("is_dir", ".git"),
            ("is_dir", ".venv"),
            ("is_file", "uv.lock"),
        ])
    
    return manifest


def generate_expected_src_files(cookiecutter_context: dict) -> list[str]:
    """Generate expected source files based on cookiecutter context."""
    src_files = BASE_SRC.copy()
    
    # Add settings.py if pydantic-settings is enabled
    if cookiecutter_context.get("use_pydantic_settings", True):
        src_files.append("settings.py")
    
    return src_files


def check_project_contents(
    project_path: Path | str,
    project_name: str,
    cookiecutter_context: dict | None = None,
) -> bool:
    """Check that the project contents match the expected manifest."""
    project_path = Path(project_path)

    assert project_path.exists()
    assert project_path.is_dir()

    # Use default context if none provided
    if cookiecutter_context is None:
        cookiecutter_context = {}

    manifest = generate_expected_manifest(cookiecutter_context)
    expected_src_files = generate_expected_src_files(cookiecutter_context)

    for content_test, content_path in manifest:
        path = project_path / content_path

        assert path.exists(), f"Expected {path} to exist"
        assert getattr(path, content_test)(), f"Expected {content_test} for {path}"

        if path.is_file():
            assert path.stat().st_size > 0, f"File {path} is unexpectedly empty"

    src = project_path / "src" / project_name
    for path in src.rglob("*.py"):
        assert path.name in expected_src_files, f"Unexpected source file: {path.name}"

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
    """Return a dictionary with common test context settings."""
    return {
        "create_github_repo": False,
        "_testing": True,  # Flag to indicate we're running tests
    }


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
