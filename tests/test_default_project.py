"""tests the contents of the generated package."""

from pathlib import Path

from .conftest import check_project_contents


def test_default_project(
    generated_template_path: Path,
    cookiecutter_package_name: str,
) -> None:
    """Tests the existence of content in the generated template."""
    assert check_project_contents(generated_template_path, cookiecutter_package_name)
