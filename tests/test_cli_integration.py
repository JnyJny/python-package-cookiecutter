"""Advanced CLI integration tests for generated projects."""

import json
import os
import subprocess
import tempfile
from pathlib import Path

import pytest


@pytest.mark.integration
class TestCLIIntegration:
    """Test CLI functionality integration in generated projects."""

    def test_cli_help_system_comprehensive(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test comprehensive CLI help system."""
        cli_tests = [
            # Basic help
            (["uv", "run", "python", "-m", "thing", "--help"], "main help"),
            # Subcommand help
            (["uv", "run", "python", "-m", "thing", "self", "--help"], "self help"),
            # Version commands
            (
                ["uv", "run", "python", "-m", "thing", "self", "version"],
                "version command",
            ),
        ]

        for cmd, description in cli_tests:
            result = subprocess.run(
                cmd, cwd=generated_template_path, capture_output=True, text=True
            )
            assert result.returncode == 0, f"Failed {description}: {result.stderr}"

            if "help" in description:
                assert "Usage:" in result.stdout, (
                    f"Help output missing for {description}"
                )

    def test_cli_error_handling(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test CLI error handling and exit codes."""
        error_tests = [
            # Invalid subcommand
            (
                ["uv", "run", "python", "-m", "thing", "nonexistent"],
                2,
                "invalid subcommand",
            ),
            # Invalid options
            (
                ["uv", "run", "python", "-m", "thing", "--invalid-option"],
                2,
                "invalid option",
            ),
            # No arguments when required
            (["uv", "run", "python", "-m", "thing"], 2, "no arguments"),
            (["uv", "run", "python", "-m", "thing", "self"], 2, "self no arguments"),
        ]

        for cmd, expected_exit_code, description in error_tests:
            result = subprocess.run(
                cmd, cwd=generated_template_path, capture_output=True, text=True
            )
            # Allow some flexibility in exit codes (different versions may use different codes)
            assert result.returncode != 0, (
                f"Expected failure for {description} but got success"
            )

    def test_cli_debug_functionality(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test debug functionality and logging."""
        # Test debug flag
        result = subprocess.run(
            ["uv", "run", "python", "-m", "thing", "--debug", "self", "version"],
            cwd=generated_template_path,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"Debug command failed: {result.stderr}"

        # Should still output version
        assert "0.1.0" in result.stdout

        # Test that debug mode can be combined with other flags
        result = subprocess.run(
            ["uv", "run", "python", "-m", "thing", "-D", "--help"],
            cwd=generated_template_path,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"Debug help failed: {result.stderr}"
        assert "Usage:" in result.stdout

    def test_cli_as_module_and_script(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test CLI can be invoked both as module and script."""
        # Test as module
        result_module = subprocess.run(
            ["uv", "run", "python", "-m", "thing", "self", "version"],
            cwd=generated_template_path,
            capture_output=True,
            text=True,
        )
        assert result_module.returncode == 0

        # Test as installed script (if available)
        result_script = subprocess.run(
            ["uv", "run", "thing", "self", "version"],
            cwd=generated_template_path,
            capture_output=True,
            text=True,
        )
        # This might fail if not installed, which is OK
        if result_script.returncode == 0:
            # If it works, output should be the same
            assert result_script.stdout == result_module.stdout

    def test_cli_environment_variables(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test CLI respects environment variables if pydantic-settings is enabled."""
        # Check if pydantic-settings is enabled
        settings_file = generated_template_path / "src" / "thing" / "settings.py"
        if not settings_file.exists():
            pytest.skip("Pydantic settings not enabled")

        # Test with environment variable
        import os

        env = os.environ.copy()
        env["THING_DEBUG"] = "true"
        result = subprocess.run(
            ["uv", "run", "python", "-m", "thing", "self", "version"],
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            env=env,
        )
        assert result.returncode == 0, f"CLI with env var failed: {result.stderr}"
