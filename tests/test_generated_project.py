"""tests the contents of the generated package."""

from pathlib import Path

# EJO This file manifest is super fragile, it should be generated from
#     template data rather than duplicated here. It's a start.

_MANIFEST = [
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

_SRC = ["__init__.py", "__main__.py", "self_subcommand.py", "settings.py"]


def test_manifest_exists_in_generated_project(
    generated_template_path: Path, cookiecutter_package_name: str
) -> None:
    """Tests the existence of content in the generated template."""
    assert generated_template_path.exists()
    assert generated_template_path.is_dir()

    for content_test, content_path in _MANIFEST:
        path = generated_template_path / content_path
        assert path.exists(), f"Expected {path} to exist in {cookiecutter_package_name}"
        assert getattr(path, content_test)()
        if path.is_file():
            assert path.stat().st_size > 0, f"File {path} is empty"

    src = generated_template_path / "src" / cookiecutter_package_name

    for path in src.rglob("*.py"):
        assert path.name in _SRC
