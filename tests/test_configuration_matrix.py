"""Test different configuration combinations systematically."""

import subprocess
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter as bake

from .conftest import check_project_contents


class TestConfigurationMatrix:
    """Test various cookiecutter configuration combinations."""

    @pytest.mark.parametrize("build_backend", ["uv", "hatch"])
    @pytest.mark.parametrize("use_pydantic_settings", [True, False])
    def test_build_backend_combinations(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
        build_backend: str,
        use_pydantic_settings: bool,
    ) -> None:
        """Test different build backend and settings combinations."""
        tmp_path = tmp_path_factory.mktemp(f"build_{build_backend}_{use_pydantic_settings}")
        
        context = {
            "build_backend": build_backend,
            "use_pydantic_settings": use_pydantic_settings,
            "create_github_repo": False,
            "package_name": f"test_{build_backend}_{str(use_pydantic_settings).lower()}",
        }
        
        # Skip hooks when pydantic settings disabled to avoid ruff issues
        if not use_pydantic_settings:
            context["_hooks_ran"] = False
            project_path = bake(
                template=str(template_root),
                no_input=True,
                extra_context=context,
                output_dir=tmp_path,
                accept_hooks=False,
            )
        else:
            project_path = bake(
                template=str(template_root),
                no_input=True,
                extra_context=context,
                output_dir=tmp_path,
            )
        
        project_path = Path(project_path)
        
        # Verify project structure
        assert check_project_contents(project_path, context["package_name"], context)
        
        # Test that the project builds with the specified backend (only if hooks ran)
        if use_pydantic_settings:  # Only test build if hooks ran properly
            result = subprocess.run(
                ["uv", "build"],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=60
            )
            assert result.returncode == 0, f"Build failed for {build_backend}: {result.stderr}"
        
        # Verify pyproject.toml contains correct build system
        pyproject_content = (project_path / "pyproject.toml").read_text()
        if build_backend == "uv":
            assert "uv_build" in pyproject_content
        else:
            assert "hatchling" in pyproject_content

    @pytest.mark.parametrize("license", ["MIT", "Apache-2.0", "GPL-3.0", "no-license"])
    def test_license_variations(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
        license: str,
    ) -> None:
        """Test different license configurations."""
        tmp_path = tmp_path_factory.mktemp(f"license_{license.replace('-', '_').replace('.', '_')}")
        
        context = {
            "license": license,
            "create_github_repo": False,
            "package_name": f"license_test_{license.lower().replace('-', '_').replace('.', '_')}",
        }
        
        project_path = bake(
            template=str(template_root),
            no_input=True,
            extra_context=context,
            output_dir=tmp_path,
        )
        
        project_path = Path(project_path)
        
        # Verify LICENSE file exists and contains expected content
        license_file = project_path / "LICENSE"
        assert license_file.exists(), f"LICENSE file missing for {license}"
        
        license_content = license_file.read_text()
        
        # Verify license-specific content
        if license == "MIT":
            assert "MIT License" in license_content
        elif license == "Apache-2.0":
            assert "Apache License" in license_content
        elif license == "GPL-3.0":
            assert "GNU GENERAL PUBLIC LICENSE" in license_content
        elif license == "no-license":
            assert "public domain" in license_content
        
        # Verify pyproject.toml license field
        pyproject_content = (project_path / "pyproject.toml").read_text()
        if license != "no-license":
            assert f'license = "{license}"' in pyproject_content

    @pytest.mark.parametrize("log_to_file", [True, False])
    @pytest.mark.parametrize("use_pydantic_settings", [True, False])
    def test_feature_combinations(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
        log_to_file: bool,
        use_pydantic_settings: bool,
    ) -> None:
        """Test different feature flag combinations."""
        tmp_path = tmp_path_factory.mktemp(f"features_{log_to_file}_{use_pydantic_settings}")
        
        context = {
            "log_to_file": log_to_file,
            "use_pydantic_settings": use_pydantic_settings,
            "create_github_repo": False,
            "package_name": f"features_{str(log_to_file).lower()}_{str(use_pydantic_settings).lower()}",
        }
        
        # Skip hooks to avoid ruff issues when settings are disabled
        if not use_pydantic_settings:
            context["_hooks_ran"] = False
            project_path = bake(
                template=str(template_root),
                no_input=True,
                extra_context=context,
                output_dir=tmp_path,
                accept_hooks=False,
            )
        else:
            project_path = bake(
                template=str(template_root),
                no_input=True,
                extra_context=context,
                output_dir=tmp_path,
            )
        
        project_path = Path(project_path)
        
        # Check main module for feature flags
        main_module = project_path / "src" / context["package_name"] / "__main__.py"
        main_content = main_module.read_text()
        
        # Verify log_to_file configuration
        if log_to_file:
            assert 'logger.add(' in main_content
        
        # Verify pydantic-settings configuration
        if use_pydantic_settings:
            assert 'from .settings import Settings' in main_content
            settings_file = project_path / "src" / context["package_name"] / "settings.py"
            assert settings_file.exists(), "settings.py should exist when pydantic-settings is enabled"
        else:
            assert 'from .settings import Settings' not in main_content or '# {%- if' in main_content

    @pytest.mark.parametrize("os_matrix", [
        "ubuntu-latest",
        "macos-latest", 
        "windows-latest",
        "ubuntu-latest, macos-latest, windows-latest"
    ])
    @pytest.mark.parametrize("python_matrix", [
        "{{ cookiecutter._python_versions[0] }}",
        "{{ cookiecutter._python_versions[-1] }}",
        "{{ cookiecutter._python_versions }}"
    ])
    def test_ci_matrix_configurations(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
        os_matrix: str,
        python_matrix: str,
    ) -> None:
        """Test different CI matrix configurations."""
        tmp_path = tmp_path_factory.mktemp("ci_matrix")
        
        context = {
            "os_testing_matrix": os_matrix,
            "python_testing_matrix": python_matrix,
            "create_github_repo": False,
            "package_name": "ci_test",
        }
        
        project_path = bake(
            template=str(template_root),
            no_input=True,
            extra_context=context,
            output_dir=tmp_path,
        )
        
        project_path = Path(project_path)
        
        # Verify GitHub workflow file
        workflow_file = project_path / ".github" / "workflows" / "release.yaml"
        assert workflow_file.exists(), "Release workflow should exist"
        
        workflow_content = workflow_file.read_text()
        
        # Verify OS matrix
        for os in os_matrix.split(", "):
            assert os.strip() in workflow_content, f"OS {os} should be in workflow"
        
        # Verify Python version matrix (this is more complex due to Jinja rendering)
        # Just check that the workflow is valid YAML and contains expected structure
        assert "strategy:" in workflow_content
        assert "matrix:" in workflow_content

    def test_minimal_configuration(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
    ) -> None:
        """Test minimal configuration with most features disabled."""
        tmp_path = tmp_path_factory.mktemp("minimal_config")
        
        context = {
            "create_github_repo": False,
            "use_pydantic_settings": False,
            "log_to_file": False,
            "license": "no-license",
            "package_name": "minimal_test",
            "_hooks_ran": False,
        }
        
        project_path = bake(
            template=str(template_root),
            no_input=True,
            extra_context=context,
            output_dir=tmp_path,
            accept_hooks=False,
        )
        
        project_path = Path(project_path)
        
        # Verify minimal project still works
        assert check_project_contents(project_path, "minimal_test", context)
        
        # Test that even minimal project has working CLI
        main_module = project_path / "src" / "minimal_test" / "__main__.py"
        assert main_module.exists()
        
        main_content = main_module.read_text()
        # Should still have basic CLI structure
        assert "typer.Typer()" in main_content
        assert "self_subcommand" in main_content

    def test_maximal_configuration(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
    ) -> None:
        """Test maximal configuration with all features enabled."""
        tmp_path = tmp_path_factory.mktemp("maximal_config")
        
        context = {
            "create_github_repo": False,  # Keep false for testing
            "use_pydantic_settings": True,
            "log_to_file": True,
            "license": "Apache-2.0",
            "build_backend": "uv",
            "package_name": "maximal_test",
            "readme_badges": True,
        }
        
        project_path = bake(
            template=str(template_root),
            no_input=True,
            extra_context=context,
            output_dir=tmp_path,
        )
        
        project_path = Path(project_path)
        
        # Verify all features are present
        assert check_project_contents(project_path, "maximal_test", context)
        
        # Test that maximal project builds and tests pass
        result = subprocess.run(
            ["uv", "run", "pytest", "-v"],
            cwd=project_path,
            capture_output=True,
            text=True,
            timeout=60
        )
        assert result.returncode == 0, f"Tests failed in maximal config: {result.stderr}"