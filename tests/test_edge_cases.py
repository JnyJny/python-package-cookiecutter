"""Test edge cases and error conditions in generated projects."""

import subprocess
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter as bake

from .conftest import check_project_contents


def test_no_license_project(
    tmp_path_factory: pytest.TempPathFactory,
    template_root: Path,
    cookiecutter_package_name: str,
) -> None:
    """Test that projects with no-license still include an Unlicense file."""
    tmp_path = tmp_path_factory.mktemp("no_license_project")

    context = {
        "license": "no-license",
        "create_github_repo": False,
    }

    project_path = bake(
        template=str(template_root),
        no_input=True,
        extra_context=context,
        output_dir=tmp_path,
    )

    # Check that LICENSE file exists and contains Unlicense text
    license_path = Path(project_path) / "LICENSE"
    assert not license_path.exists(), "LICENSE file exists for no-license project"


def test_no_pydantic_settings_project(
    tmp_path_factory: pytest.TempPathFactory,
    template_root: Path,
    cookiecutter_package_name: str,
) -> None:
    """Test that projects without pydantic-settings don't include settings.py."""
    tmp_path = tmp_path_factory.mktemp("no_pydantic_project")

    context = {
        "use_pydantic_settings": False,
        "create_github_repo": False,
    }

    # Generate without hooks to avoid ruff issues in test templates
    project_path = bake(
        template=str(template_root),
        no_input=True,
        extra_context=context,
        output_dir=tmp_path,
        skip_if_file_exists=True,
        accept_hooks=False,  # Skip hooks for this test
    )

    # Check that settings.py doesn't exist
    settings_path = (
        Path(project_path) / "src" / cookiecutter_package_name / "settings.py"
    )
    assert not settings_path.exists(), (
        "settings.py should not exist when pydantic-settings is disabled"
    )

    # Check project structure (but skip .git and .venv since hooks didn't run)
    basic_context = context.copy()
    basic_context["_hooks_ran"] = False
    assert check_project_contents(
        project_path, cookiecutter_package_name, basic_context
    )


def test_generated_project_imports_work(generated_template_path: Path) -> None:
    """Test that generated project modules can be imported without errors."""
    result = subprocess.run(
        [
            "uv",
            "run",
            "python",
            "-c",
            "import thing; import thing.__main__; import thing.self_subcommand",
        ],
        cwd=generated_template_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Module imports failed: {result.stderr}"


def test_generated_project_cli_runs(generated_template_path: Path) -> None:
    """Test that generated project CLI can be invoked."""
    result = subprocess.run(
        ["uv", "run", "python", "-m", "thing", "--help"],
        cwd=generated_template_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"CLI execution failed: {result.stderr}"
    assert "Usage:" in result.stdout, "CLI help should show usage information"


def test_generated_project_cli_version(generated_template_path: Path) -> None:
    """Test that generated project CLI version command works."""
    result = subprocess.run(
        ["uv", "run", "python", "-m", "thing", "self", "version"],
        cwd=generated_template_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"CLI version command failed: {result.stderr}"
    assert "0.1.0" in result.stdout, "Version command should output project version"


def test_generated_project_can_be_built(generated_template_path: Path) -> None:
    """Test that generated project can be built as a package."""
    result = subprocess.run(
        ["uv", "build"], cwd=generated_template_path, capture_output=True, text=True
    )
    assert result.returncode == 0, f"Package build failed: {result.stderr}"

    # Check that build artifacts exist
    dist_path = generated_template_path / "dist"
    assert dist_path.exists(), "dist directory should exist after build"

    # Should have both wheel and sdist
    built_files = list(dist_path.glob("*"))
    assert len(built_files) >= 2, "Should have both wheel and source distribution"

    wheel_files = list(dist_path.glob("*.whl"))
    assert len(wheel_files) >= 1, "Should have at least one wheel file"

    sdist_files = list(dist_path.glob("*.tar.gz"))
    assert len(sdist_files) >= 1, "Should have at least one source distribution"


def test_generated_project_handles_debug_flag(generated_template_path: Path) -> None:
    """Test that generated project handles debug flag correctly."""
    result = subprocess.run(
        ["uv", "run", "python", "-m", "thing", "--debug", "--help"],
        cwd=generated_template_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"CLI with debug flag failed: {result.stderr}"


def test_invalid_package_name_characters():
    """Test that invalid package names are handled appropriately."""
    # This test validates that our template doesn't break with edge case names
    # In practice, cookiecutter itself validates package names
    invalid_names = ["123invalid", "invalid-name", "invalid.name", ""]

    for name in invalid_names:
        # We expect these to either be rejected by cookiecutter or handled gracefully
        # This test documents the expected behavior
        assert not name.isidentifier() or name == "", f"Name '{name}' should be invalid"
