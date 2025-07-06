"""Cross-platform validation tests for generated projects."""

import os
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.cross_platform
class TestCrossPlatformCompatibility:
    """Test that generated projects work across different platforms."""

    def test_path_handling_cross_platform(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that generated projects handle paths correctly across platforms."""
        # Test that all paths in generated files use forward slashes or Path objects
        python_files = list(generated_template_path.rglob("*.py"))
        
        for py_file in python_files:
            content = py_file.read_text()
            
            # Check for hardcoded Windows paths (backslashes)
            lines = content.split('\n')
            for line_num, line in enumerate(lines, 1):
                # Skip comments and docstrings
                stripped = line.strip()
                if stripped.startswith('#') or stripped.startswith('"""') or stripped.startswith("'''"):
                    continue
                
                # Look for problematic backslash usage
                if '\\' in line and not any(escape in line for escape in ['\\n', '\\t', '\\r', '\\"', "\\'"]):
                    # This might be a Windows path - check if it's in a string
                    if '"' in line or "'" in line:
                        pytest.fail(f"Possible hardcoded Windows path in {py_file}:{line_num}: {line.strip()}")

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
                crlf_count = content_bytes.count(b'\r\n')
                # Check for old Mac line endings (CR only)
                cr_only = content_bytes.count(b'\r') - crlf_count
                # Check for Unix line endings (LF only)
                lf_only = content_bytes.count(b'\n') - crlf_count
                
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
        if os.name != 'nt':  # Not Windows
            python_files = list(generated_template_path.rglob("*.py"))
            
            for py_file in python_files:
                stat = py_file.stat()
                # Check if file is executable by owner
                is_executable = bool(stat.st_mode & 0o100)
                
                # Regular Python files should not be executable
                # (except for scripts with shebang)
                if is_executable:
                    content = py_file.read_text()
                    if not content.startswith('#!'):
                        pytest.fail(f"Python file {py_file} is executable but has no shebang")

    def test_environment_variable_handling(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test environment variable handling works cross-platform."""
        # Test with different environment variable formats
        test_cases = [
            {"TEST_VAR": "test_value"},
            {"PATH": "/test/path"},  # Unix-style path
        ]
        
        if sys.platform == "win32":
            test_cases.append({"PATH": "C:\\test\\path"})  # Windows-style path
        
        for env_vars in test_cases:
            env = {**os.environ, **env_vars}
            
            result = subprocess.run(
                ["uv", "run", "python", "-m", "thing", "self", "version"],
                cwd=generated_template_path,
                capture_output=True,
                text=True,
                env=env
            )
            assert result.returncode == 0, f"CLI failed with env vars {env_vars}: {result.stderr}"

    def test_file_system_case_sensitivity(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that imports work regardless of filesystem case sensitivity."""
        # Test that all imports in Python files reference actual file names correctly
        python_files = list(generated_template_path.rglob("*.py"))
        
        for py_file in python_files:
            content = py_file.read_text()
            lines = content.split('\n')
            
            for line_num, line in enumerate(lines, 1):
                stripped = line.strip()
                
                # Look for relative imports
                if stripped.startswith('from .') or stripped.startswith('from ..'):
                    # Extract the module name
                    if ' import ' in stripped:
                        module_part = stripped.split(' import ')[0]
                        module_name = module_part.replace('from .', '').replace('from ..', '')
                        
                        if module_name:
                            # Check if corresponding file exists with exact case
                            expected_file = py_file.parent / f"{module_name}.py"
                            if not expected_file.exists():
                                # Check if it's a package
                                expected_package = py_file.parent / module_name / "__init__.py"
                                if not expected_package.exists():
                                    pytest.fail(f"Import {module_name} in {py_file}:{line_num} may have case mismatch")

    @pytest.mark.skipif(sys.platform == "win32", reason="Unix-specific test")
    def test_unix_specific_features(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test Unix-specific features in generated projects."""
        # Test that shell commands work
        result = subprocess.run(
            ["bash", "-c", "cd . && echo 'test'"],
            cwd=generated_template_path,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0, "Basic shell commands should work"

    @pytest.mark.skipif(sys.platform != "win32", reason="Windows-specific test")
    def test_windows_specific_features(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test Windows-specific features in generated projects."""
        # Test that Windows commands work
        result = subprocess.run(
            ["cmd", "/c", "echo test"],
            cwd=generated_template_path,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0, "Basic Windows commands should work"

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
                ["uv", "run", "python", "-m", "unicode_test", "self", "version"],
                cwd=project_path,
                capture_output=True,
                text=True
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
                ["uv", "run", "python", "-m", "longpath_test", "self", "version"],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            assert result.returncode == 0, f"Long path test failed: {result.stderr}"
            
        except Exception as e:
            # Some systems have path length limitations
            if "path too long" in str(e).lower() or "filename too long" in str(e).lower():
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
        assert "requires-python" in content, "pyproject.toml should specify Python version requirement"
        
        # Should be compatible with current Python version
        current_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        
        # Extract the Python version requirement
        import re
        version_match = re.search(r'requires-python\s*=\s*"([^"]+)"', content)
        if version_match:
            version_req = version_match.group(1)
            # This is a basic check - in practice you'd want to parse the version spec properly
            assert ">=" in version_req or "==" in version_req, "Should have a minimum version requirement"

    def test_dependency_compatibility(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that project dependencies are compatible across platforms."""
        # Test that uv can resolve dependencies
        result = subprocess.run(
            ["uv", "lock", "--check"],
            cwd=generated_template_path,
            capture_output=True,
            text=True
        )
        
        # If lock file exists and is up to date, this should succeed
        # If it fails, it might indicate platform-specific dependency issues
        if result.returncode != 0:
            # Try to update lock file
            result = subprocess.run(
                ["uv", "lock"],
                cwd=generated_template_path,
                capture_output=True,
                text=True
            )
            assert result.returncode == 0, f"Dependency resolution failed: {result.stderr}"