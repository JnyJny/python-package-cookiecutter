"""Build process validation tests for generated projects."""

import os
import shutil
import subprocess
import tarfile
import zipfile
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter as bake


class TestBuildValidation:
    """Test that generated projects build correctly and produce valid packages."""

    def test_package_builds_successfully(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that package builds without errors."""
        result = subprocess.run(
            ["uv", "build"],  # noqa: S607
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Package build failed: {result.stderr}"

        # Check that dist directory was created
        dist_dir = generated_template_path / "dist"
        assert dist_dir.exists(), "dist directory should be created during build"

        # Check that build artifacts exist
        built_files = list(dist_dir.glob("*"))
        assert len(built_files) > 0, "Build should produce artifacts"

    def test_wheel_package_structure(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that built wheel has correct structure."""
        # Build the package
        result = subprocess.run(
            ["uv", "build"],  # noqa: S607
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Build failed: {result.stderr}"

        # Find the wheel file
        dist_dir = generated_template_path / "dist"
        wheel_files = list(dist_dir.glob("*.whl"))
        assert len(wheel_files) >= 1, "Should produce at least one wheel file"

        wheel_file = wheel_files[0]

        # Extract and examine wheel contents
        with zipfile.ZipFile(wheel_file, "r") as wheel:
            wheel_contents = wheel.namelist()

            # Should contain the package
            package_files = [f for f in wheel_contents if f.startswith("thing/")]
            assert len(package_files) > 0, "Wheel should contain package files"

            # Should contain metadata
            metadata_files = [
                f for f in wheel_contents if f.endswith(".dist-info/METADATA")
            ]
            assert len(metadata_files) == 1, (
                "Wheel should contain exactly one METADATA file"
            )

            # Should contain entry points if CLI is configured
            entry_point_files = [
                f for f in wheel_contents if f.endswith(".dist-info/entry_points.txt")
            ]
            if entry_point_files:
                # Read entry points
                with wheel.open(entry_point_files[0]) as ep_file:
                    entry_points = ep_file.read().decode("utf-8")
                    assert "[console_scripts]" in entry_points, (
                        "Should have console scripts"
                    )
                    assert "thing =" in entry_points, "Should have CLI entry point"

    def test_source_distribution_structure(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that built source distribution has correct structure."""
        # Build the package
        result = subprocess.run(
            ["uv", "build"],  # noqa: S607
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Build failed: {result.stderr}"

        # Find the source distribution
        dist_dir = generated_template_path / "dist"
        sdist_files = list(dist_dir.glob("*.tar.gz"))
        assert len(sdist_files) >= 1, "Should produce at least one source distribution"

        sdist_file = sdist_files[0]

        # Extract and examine sdist contents
        with tarfile.open(sdist_file, "r:gz") as sdist:
            sdist_contents = sdist.getnames()

            # Should contain source files
            src_files = [
                f for f in sdist_contents if "/src/" in f and f.endswith(".py")
            ]
            assert len(src_files) > 0, "Source distribution should contain source files"

            # Should contain pyproject.toml
            pyproject_files = [
                f for f in sdist_contents if f.endswith("pyproject.toml")
            ]
            assert len(pyproject_files) == 1, "Should contain pyproject.toml"

            # Should contain README
            readme_files = [f for f in sdist_contents if f.endswith("README.md")]
            assert len(readme_files) == 1, "Should contain README.md"

    def test_package_metadata_validity(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that package metadata is valid."""
        # Build the package
        result = subprocess.run(
            ["uv", "build"],  # noqa: S607
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Build failed: {result.stderr}"

        # Check wheel metadata
        dist_dir = generated_template_path / "dist"
        wheel_files = list(dist_dir.glob("*.whl"))

        with zipfile.ZipFile(wheel_files[0], "r") as wheel:
            metadata_files = [
                f for f in wheel.namelist() if f.endswith(".dist-info/METADATA")
            ]

            with wheel.open(metadata_files[0]) as metadata_file:
                metadata = metadata_file.read().decode("utf-8")

                # Check required fields
                assert "Name: thing" in metadata, "Should have package name"
                assert "Version: 0.1.0" in metadata, "Should have version"
                assert "Summary:" in metadata, "Should have summary"
                assert "Author:" in metadata or "Author-Email:" in metadata, (
                    "Should have author info"
                )

                # Check classifiers
                assert "Classifier:" in metadata, "Should have classifiers"

    def test_package_installation_from_wheel(
        self,
        generated_template_path: Path,
        tmp_path_factory: pytest.TempPathFactory,
    ) -> None:
        """Test that built wheel can be installed and used."""
        # Build the package
        result = subprocess.run(
            ["uv", "build"],  # noqa: S607
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Build failed: {result.stderr}"

        # Create a test environment
        test_env = tmp_path_factory.mktemp("install_test")

        result = subprocess.run(
            ["uv", "venv", str(test_env / "venv")],  # noqa: S607
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, (
            f"Virtual environment creation failed: {result.stderr}"
        )

        # Install the wheel
        dist_dir = generated_template_path / "dist"
        wheel_files = list(dist_dir.glob("*.whl"))

        env = os.environ.copy()
        env["VIRTUAL_ENV"] = str(test_env / "venv")

        result = subprocess.run(
            ["uv", "pip", "install", str(wheel_files[0])],  # noqa: S607
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Wheel installation failed: {result.stderr}"

        # Test that installed package works
        venv_python = test_env / "venv" / "bin" / "python"
        if not venv_python.exists():
            venv_python = test_env / "venv" / "Scripts" / "python.exe"  # Windows

        if venv_python.exists():
            result = subprocess.run(
                [str(venv_python), "-c", "import thing; print('Import successful')"],
                capture_output=True,
                text=True,
                check=False,
            )
            assert result.returncode == 0, (
                f"Installed package import failed: {result.stderr}"
            )
            assert "Import successful" in result.stdout

    def test_build_reproducibility(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that builds are reproducible."""
        # Build once
        result1 = subprocess.run(
            ["uv", "build"],  # noqa: S607
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result1.returncode == 0, f"First build failed: {result1.stderr}"

        # Get first build artifacts
        dist_dir = generated_template_path / "dist"
        first_files = {f.name: f.stat().st_size for f in dist_dir.glob("*")}

        # Clean and build again
        shutil.rmtree(dist_dir, ignore_errors=True)

        result2 = subprocess.run(
            ["uv", "build"],  # noqa: S607
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result2.returncode == 0, f"Second build failed: {result2.stderr}"

        # Get second build artifacts
        second_files = {f.name: f.stat().st_size for f in dist_dir.glob("*")}

        # Compare builds (sizes should be the same for reproducible builds)
        assert first_files.keys() == second_files.keys(), (
            "Build artifacts should be the same"
        )

        for (f_name, f_size), (s_name, s_size) in zip(
            first_files.items(), second_files.items(), strict=False
        ):
            assert f_name == s_name, f"File {f_name} differs from {s_name}"
            assert f_size == s_size, f"File {f_name} size differs {f_size} != {s_size}"

    def test_build_with_different_backends(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
        cookiecutter_extra_context: dict,
    ) -> None:
        """Test building with different build backends."""
        backends_to_test = ["uv", "hatch"]

        for backend in backends_to_test:
            tmp_path = tmp_path_factory.mktemp(f"build_{backend}")

            cookiecutter_extra_context |= {
                "build_backend": backend,
                "package_name": f"build_test_{backend}",
            }

            project_path = bake(
                template=str(template_root),
                no_input=True,
                extra_context=cookiecutter_extra_context,
                output_dir=tmp_path,
            )

            # Test build
            result = subprocess.run(
                ["uv", "build"],  # noqa: S607
                cwd=project_path,
                capture_output=True,
                text=True,
                check=False,
            )
            assert result.returncode == 0, (
                f"Build with {backend} backend failed: {result.stderr}"
            )

            # Check artifacts exist
            dist_dir = Path(project_path) / "dist"
            wheel_files = list(dist_dir.glob("*.whl"))
            sdist_files = list(dist_dir.glob("*.tar.gz"))

            assert len(wheel_files) >= 1, f"No wheel produced with {backend} backend"
            assert len(sdist_files) >= 1, f"No sdist produced with {backend} backend"

    def test_package_size_reasonable(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that built packages are reasonably sized."""
        # Build the package
        result = subprocess.run(
            ["uv", "build"],  # noqa: S607
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Build failed: {result.stderr}"

        dist_dir = generated_template_path / "dist"
        k = 1024
        # Check wheel size
        wheel_files = list(dist_dir.glob("*.whl"))
        for wheel_file in wheel_files:
            wheel_size = wheel_file.stat().st_size / k  # KB
            assert wheel_size < k, (
                f"Wheel {wheel_file.name} is too large: {wheel_size:.1f}KB"
            )
            assert wheel_size > 1, (
                f"Wheel {wheel_file.name} is suspiciously small: {wheel_size:.1f}KB"
            )

        # Check sdist size
        sdist_files = list(dist_dir.glob("*.tar.gz"))
        for sdist_file in sdist_files:
            sdist_size = sdist_file.stat().st_size / k  # KB
            assert sdist_size < 2 * k, (
                f"Sdist {sdist_file.name} is too large: {sdist_size:.1f}KB"
            )
            assert sdist_size > 1, (
                f"Sdist {sdist_file.name} is suspiciously small: {sdist_size:.1f}KB"
            )

    def test_clean_build_environment(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that build works in clean environment."""
        # Remove any existing build artifacts
        dist_dir = generated_template_path / "dist"
        build_dir = generated_template_path / "build"

        for artifacts in [dist_dir, build_dir]:
            shutil.rmtree(artifacts, ignore_errors=True)

        # Build in clean state
        result = subprocess.run(
            ["uv", "build"],  # noqa: S607
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Clean build failed: {result.stderr}"

        # Verify artifacts were created
        assert dist_dir.exists(), "dist directory should be created"

        built_files = list(dist_dir.glob("*"))
        assert built_files, "Should produce both wheel and sdist"

    def test_version_consistency(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that version is consistent across all package metadata."""
        # Check pyproject.toml version
        pyproject_file = generated_template_path / "pyproject.toml"
        pyproject_content = pyproject_file.read_text()

        import re

        version_match = re.search(r'version\s*=\s*"([^"]+)"', pyproject_content)
        assert version_match, "Should find version in pyproject.toml"
        pyproject_version = version_match.group(1)

        # Build and check wheel metadata version
        result = subprocess.run(
            ["uv", "build"],  # noqa: S607
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, f"Build failed: {result.stderr}"

        dist_dir = generated_template_path / "dist"
        wheel_files = list(dist_dir.glob("*.whl"))

        with zipfile.ZipFile(wheel_files[0], "r") as wheel:
            metadata_files = [
                f for f in wheel.namelist() if f.endswith(".dist-info/METADATA")
            ]

            with wheel.open(metadata_files[0]) as metadata_file:
                metadata = metadata_file.read().decode("utf-8")

                metadata_version_match = re.search(
                    r"^Version:\s*([^\s]+)", metadata, re.MULTILINE
                )
                assert metadata_version_match, "Should find version in wheel metadata"
                metadata_version = metadata_version_match.group(1)

                assert pyproject_version == metadata_version, (
                    "Versions should match between pyproject.toml and wheel metadata"
                )
