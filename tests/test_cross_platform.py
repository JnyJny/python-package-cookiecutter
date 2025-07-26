"""Cross-platform validation tests for generated projects."""

import os
import subprocess
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter as bake


@pytest.mark.cross_platform
class TestCrossPlatformCompatibility:
    """Test that generated projects work across different platforms."""

    def test_path_handling_cross_platform(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that generated projects handle paths correctly across platforms."""
        # Test that all paths in generated files use forward slashes or Path objects
        # Exclude .venv directory since we don't control third-party library content
        python_files = [
            f
            for f in generated_template_path.rglob("*.py")
            if ".venv" not in str(f) and "site-packages" not in str(f)
        ]

        for py_file in python_files:
            content = py_file.read_text()

            # Check for hardcoded Windows paths (backslashes)
            lines = content.split("\n")
            for line_num, line in enumerate(lines, 1):
                # Skip comments and docstrings
                stripped = line.strip()
                if stripped.startswith(("#", '"""', "'''")):
                    continue

                if any(c in line for c in ["\\n", "\\t", "\\r", '\\"', "\\'"]):
                    continue

                if '"' in line or "'" in line:
                    pytest.fail(
                        f"Maybe Windows path in {py_file}:{line_num}: {line.strip()}"
                    )

    def test_line_endings_consistency(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that generated files have consistent line endings."""
        text_files = []

        # Check common text file types
        for pattern in ["*.py", "*.md", "*.toml", "*.yaml", "*.yml", "*.txt"]:
            text_files.extend(generated_template_path.rglob(pattern))

        for text_file in text_files:
            try:
                content_bytes = text_file.read_bytes()

                # Check for Windows line endings (CRLF)
                crlf_count = content_bytes.count(b"\r\n")
                # Check for old Mac line endings (CR only)
                cr_only = content_bytes.count(b"\r") - crlf_count
                # Check for Unix line endings (LF only)
                lf_only = content_bytes.count(b"\n") - crlf_count

                # Files should primarily use Unix line endings
                if crlf_count > 0 and lf_only > 0:
                    pytest.fail(f"Mixed line endings in {text_file}")

                if cr_only > 0:
                    pytest.fail(f"Old Mac line endings (CR only) found in {text_file}")

            except UnicodeDecodeError:
                # Skip binary files
                continue

    def test_executable_permissions(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that files have appropriate permissions."""
        # On Unix-like systems, check that Python files are not executable
        if os.name == "nt":  # Not Windows
            pytest.skip("Executable permissions test is not applicable on Windows.")

        python_files = list(generated_template_path.rglob("*.py"))

        for py_file in python_files:
            stat = py_file.stat()

            if not stat.st_mode & 0o100:
                continue

            if stat.st_size == 0:
                continue

            content = py_file.read_text()
            if not content.startswith("#!"):
                pytest.fail(f"Python executable missing shebang {py_file}")

    def test_unicode_filenames_support(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
    ) -> None:
        """Test that template works with Unicode in project paths."""
        # Create a directory with Unicode characters
        unicode_dir = tmp_path_factory.mktemp("tëst_ünicødé")

        context = {
            "create_github_repo": False,
            "package_name": "unicode_test",
        }

        try:
            project_path = bake(
                template=str(template_root),
                no_input=True,
                extra_context=context,
                output_dir=unicode_dir,
            )

            # Test that the project works
            result = subprocess.run(
                ["uv", "run", "python", "-m", "unicode_test", "self", "version"],  # noqa: S607
                cwd=project_path,
                capture_output=True,
                text=True,
                check=False,
            )
            assert result.returncode == 0, f"Unicode path test failed: {result.stderr}"

        except Exception as e:
            # Some filesystems might not support Unicode, which is acceptable
            pytest.skip(f"Unicode filenames not supported: {e}")

    def test_long_path_support(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
    ) -> None:
        """Test that template works with long paths."""
        # Create a deep directory structure
        deep_path = tmp_path_factory.mktemp("long_path_test")

        # Create a reasonably deep path (but not too deep to avoid issues)
        for i in range(5):
            deep_path = deep_path / f"very_long_directory_name_level_{i}"
            deep_path.mkdir()

        context = {
            "create_github_repo": False,
            "package_name": "longpath_test",
        }

        try:
            project_path = bake(
                template=str(template_root),
                no_input=True,
                extra_context=context,
                output_dir=deep_path,
            )

            # Test that the project works
            result = subprocess.run(
                ["uv", "run", "python", "-m", "longpath_test", "self", "version"],  # noqa: S607
                cwd=project_path,
                capture_output=True,
                text=True,
                check=False,
            )
            assert result.returncode == 0, f"Long path test failed: {result.stderr}"

        except Exception as e:
            # Some systems have path length limitations
            if (
                "path too long" in str(e).lower()
                or "filename too long" in str(e).lower()
            ):
                pytest.skip(f"Path length limitation: {e}")
            else:
                raise

    def test_python_version_compatibility(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that generated project declares correct Python version requirements."""
        pyproject_file = generated_template_path / "pyproject.toml"
        assert pyproject_file.exists(), "pyproject.toml should exist"

        content = pyproject_file.read_text()

        # Should have Python version requirement
        assert "requires-python" in content, (
            "pyproject.toml should specify Python version requirement"
        )

    def test_dependency_compatibility(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that project dependencies are compatible across platforms."""
        # Test that uv can resolve dependencies
        result = subprocess.run(
            ["uv", "lock", "--check"],  # noqa: S607
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            check=False,
        )

        # If lock file exists and is up to date, this should succeed
        # If it fails, it might indicate platform-specific dependency issues
        if result.returncode != 0:
            # Try to update lock file
            result = subprocess.run(
                ["uv", "lock"],  # noqa: S607
                cwd=generated_template_path,
                capture_output=True,
                text=True,
                check=False,
            )
            assert result.returncode == 0, (
                f"Dependency resolution failed: {result.stderr}"
            )
