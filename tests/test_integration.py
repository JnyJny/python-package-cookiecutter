"""Integration tests for end-to-end workflows in generated projects."""

import os
import subprocess
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter as bake


@pytest.mark.integration
class TestWorkflowIntegration:
    """Test complete development workflows in generated projects."""

    def test_full_development_cycle(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
        cookiecutter_package_name: str,
    ) -> None:
        """Test complete development workflow from generation to build."""
        tmp_path = tmp_path_factory.mktemp("full_dev_cycle")

        context = {
            "create_github_repo": False,
            "use_pydantic_settings": True,
            "log_to_file": True,
        }

        # Generate project
        project_path = bake(
            template=str(template_root),
            no_input=True,
            extra_context=context,
            output_dir=tmp_path,
        )

        project_path = Path(project_path)

        # Test development workflow sequence
        workflow_steps = [
            (["uv", "run", "pytest"], "Tests should pass"),
            (["uv", "run", "poe", "ruff"], "Code should be properly formatted"),
            (["uv", "run", "poe", "mypy"], "Type checking should pass"),
            (["uv", "run", "poe", "ty"], "Alternative type checker should pass"),
            (["uv", "build"], "Package should build successfully"),
        ]

        for cmd, description in workflow_steps:
            result = subprocess.run(
                cmd,
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
            )
            assert result.returncode == 0, (
                f"{description}. Command failed: {' '.join(cmd)}\nStderr: {result.stderr}"
            )

    def test_cli_workflow_integration(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
        cookiecutter_package_name: str,
    ) -> None:
        """Test CLI functionality integration."""
        tmp_path = tmp_path_factory.mktemp("cli_integration")

        context = {
            "create_github_repo": False,
            "cli_name": "testcli",
            "package_name": "testpackage",
        }

        project_path = bake(
            template=str(template_root),
            no_input=True,
            extra_context=context,
            output_dir=tmp_path,
        )

        # Test CLI installation and usage
        project_path = Path(project_path)

        # Install package in development mode
        result = subprocess.run(
            ["uv", "pip", "install", "-e", "."],
            cwd=project_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Package installation failed: {result.stderr}"

        # Test CLI commands
        cli_tests = [
            (["uv", "run", "testcli", "--help"], "CLI help should work"),
            (["uv", "run", "testcli", "--debug", "--help"], "Debug mode should work"),
            (
                ["uv", "run", "testcli", "self", "--help"],
                "Self subcommand help should work",
            ),
            (
                ["uv", "run", "testcli", "self", "version"],
                "Version command should work",
            ),
        ]

        for cmd, description in cli_tests:
            result = subprocess.run(
                cmd, cwd=project_path, capture_output=True, text=True, check=False
            )
            assert result.returncode == 0, (
                f"{description}. Command: {' '.join(cmd)}\nStderr: {result.stderr}"
            )

    def test_settings_integration(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
    ) -> None:
        """Test pydantic-settings integration works end-to-end."""
        tmp_path = tmp_path_factory.mktemp("settings_integration")

        context = {
            "create_github_repo": False,
            "use_pydantic_settings": True,
            "package_name": "settingstest",
        }

        project_path = bake(
            template=str(template_root),
            no_input=True,
            extra_context=context,
            output_dir=tmp_path,
        )

        project_path = Path(project_path)

        # Test that settings can be imported and used
        test_script = project_path / "test_settings.py"
        test_script.write_text("""
import sys
sys.path.insert(0, 'src')

from settingstest.settings import Settings

# Test settings instantiation
settings = Settings()
assert hasattr(settings, 'debug')
print("Settings integration test passed")
""")

        result = subprocess.run(
            ["uv", "run", "python", "test_settings.py"],
            cwd=project_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Settings integration failed: {result.stderr}"
        assert "Settings integration test passed" in result.stdout

    def test_logging_integration(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that logging integration works properly."""
        # Test logging to file when enabled
        result = subprocess.run(
            ["uv", "run", "python", "-m", "thing", "--debug", "self", "version"],
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Logging test failed: {result.stderr}"

        # Check if log file was created (based on default template settings)
        log_file = generated_template_path / "thing.log"
        if log_file.exists():
            assert log_file.stat().st_size > 0, "Log file should contain content"

    def test_package_installation_workflow(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
    ) -> None:
        """Test that generated packages can be installed and used."""
        tmp_path = tmp_path_factory.mktemp("install_test")

        context = {
            "create_github_repo": False,
            "package_name": "installtest",
            "cli_name": "installtest-cli",
        }

        project_path = bake(
            template=str(template_root),
            no_input=True,
            extra_context=context,
            output_dir=tmp_path,
        )

        project_path = Path(project_path)

        # Build the package
        result = subprocess.run(
            ["uv", "build"],
            cwd=project_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Package build failed: {result.stderr}"

        # Test that wheel can be installed
        wheel_files = list((project_path / "dist").glob("*.whl"))
        assert len(wheel_files) > 0, "No wheel file found"

        # Create a test environment and install
        test_env = tmp_path / "test_env"
        result = subprocess.run(
            ["uv", "venv", str(test_env)], capture_output=True, text=True, check=False
        )
        assert result.returncode == 0, (
            f"Test environment creation failed: {result.stderr}"
        )

        # Install the package
        # Need to inherit PATH and other env vars for uv to work

        env = os.environ.copy()
        env["VIRTUAL_ENV"] = str(test_env)

        result = subprocess.run(
            ["uv", "pip", "install", str(wheel_files[0])],
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Package installation failed: {result.stderr}"
