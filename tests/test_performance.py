"""Performance and benchmarking tests for template generation and projects."""

import subprocess
import time
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter as bake


@pytest.mark.performance
class TestPerformance:
    """Performance benchmarking and regression tests."""

    def test_template_generation_speed(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
    ) -> None:
        """Benchmark template generation speed."""
        tmp_path = tmp_path_factory.mktemp("speed_test")
        
        context = {
            "create_github_repo": False,
            "package_name": "speed_test",
        }
        
        # Measure template generation time
        start_time = time.time()
        
        project_path = bake(
            template=str(template_root),
            no_input=True,
            extra_context=context,
            output_dir=tmp_path,
        )
        
        generation_time = time.time() - start_time
        
        # Assert reasonable generation time (should be under 30 seconds)
        assert generation_time < 30.0, f"Template generation took {generation_time:.2f}s, which is too slow"
        
        # Verify project was actually created
        assert Path(project_path).exists()
        
        print(f"Template generation time: {generation_time:.2f} seconds")

    def test_build_performance(
        self,
        generated_template_path: Path,
    ) -> None:
        """Benchmark build performance of generated projects."""
        # Measure build time
        start_time = time.time()
        
        result = subprocess.run(
            ["uv", "build"],
            cwd=generated_template_path,
            capture_output=True,
            text=True
        )
        
        build_time = time.time() - start_time
        
        assert result.returncode == 0, f"Build failed: {result.stderr}"
        
        # Assert reasonable build time (should be under 60 seconds)
        assert build_time < 60.0, f"Build took {build_time:.2f}s, which is too slow"
        
        print(f"Build time: {build_time:.2f} seconds")

    def test_test_execution_performance(
        self,
        generated_template_path: Path,
    ) -> None:
        """Benchmark test execution speed in generated projects."""
        # Measure test execution time
        start_time = time.time()
        
        result = subprocess.run(
            ["uv", "run", "pytest", "-v"],
            cwd=generated_template_path,
            capture_output=True,
            text=True
        )
        
        test_time = time.time() - start_time
        
        assert result.returncode == 0, f"Tests failed: {result.stderr}"
        
        # Assert reasonable test time (should be under 30 seconds)
        assert test_time < 30.0, f"Test execution took {test_time:.2f}s, which is too slow"
        
        print(f"Test execution time: {test_time:.2f} seconds")

    def test_linting_performance(
        self,
        generated_template_path: Path,
    ) -> None:
        """Benchmark linting performance in generated projects."""
        # Measure ruff execution time
        start_time = time.time()
        
        result = subprocess.run(
            ["uv", "run", "poe", "ruff"],
            cwd=generated_template_path,
            capture_output=True,
            text=True
        )
        
        lint_time = time.time() - start_time
        
        assert result.returncode == 0, f"Linting failed: {result.stderr}"
        
        # Assert reasonable lint time (should be under 15 seconds)
        assert lint_time < 15.0, f"Linting took {lint_time:.2f}s, which is too slow"
        
        print(f"Linting time: {lint_time:.2f} seconds")

    def test_type_checking_performance(
        self,
        generated_template_path: Path,
    ) -> None:
        """Benchmark type checking performance in generated projects."""
        # Measure mypy execution time
        start_time = time.time()
        
        result = subprocess.run(
            ["uv", "run", "poe", "mypy"],
            cwd=generated_template_path,
            capture_output=True,
            text=True
        )
        
        mypy_time = time.time() - start_time
        
        assert result.returncode == 0, f"Type checking failed: {result.stderr}"
        
        # Assert reasonable mypy time (should be under 20 seconds)
        assert mypy_time < 20.0, f"Type checking took {mypy_time:.2f}s, which is too slow"
        
        print(f"Type checking time: {mypy_time:.2f} seconds")

    @pytest.mark.parametrize("operation", ["test", "ruff", "mypy"])
    def test_repeated_operation_performance(
        self,
        generated_template_path: Path,
        operation: str,
    ) -> None:
        """Test that repeated operations don't degrade in performance."""
        times = []
        
        for i in range(3):
            start_time = time.time()
            
            result = subprocess.run(
                ["uv", "run", "poe", operation],
                cwd=generated_template_path,
                capture_output=True,
                text=True
            )
            
            execution_time = time.time() - start_time
            times.append(execution_time)
            
            assert result.returncode == 0, f"{operation} failed on run {i+1}: {result.stderr}"
        
        # Check that performance doesn't degrade significantly
        # Second and third runs should not be more than 50% slower than first
        first_time = times[0]
        for i, run_time in enumerate(times[1:], 2):
            slowdown_factor = run_time / first_time
            assert slowdown_factor < 1.5, f"Run {i} was {slowdown_factor:.2f}x slower than first run"
        
        print(f"{operation} times: {[f'{t:.2f}s' for t in times]}")

    def test_memory_usage_during_generation(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
    ) -> None:
        """Test memory usage during template generation (basic monitoring)."""
        import psutil
        import os
        
        tmp_path = tmp_path_factory.mktemp("memory_test")
        
        context = {
            "create_github_repo": False,
            "package_name": "memory_test",
        }
        
        # Get baseline memory usage
        process = psutil.Process(os.getpid())
        baseline_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        # Generate template
        project_path = bake(
            template=str(template_root),
            no_input=True,
            extra_context=context,
            output_dir=tmp_path,
        )
        
        # Check memory usage after generation
        peak_memory = process.memory_info().rss / 1024 / 1024  # MB
        memory_increase = peak_memory - baseline_memory
        
        # Assert reasonable memory usage (should not increase by more than 200MB)
        assert memory_increase < 200, f"Memory usage increased by {memory_increase:.2f}MB during generation"
        
        # Verify project was created
        assert Path(project_path).exists()
        
        print(f"Memory increase during generation: {memory_increase:.2f} MB")

    def test_concurrent_generation_performance(
        self,
        tmp_path_factory: pytest.TempPathFactory,
        template_root: Path,
    ) -> None:
        """Test performance when generating multiple projects concurrently."""
        import concurrent.futures
        import threading
        
        def generate_project(project_id: int) -> tuple[int, float]:
            """Generate a single project and return timing."""
            tmp_path = tmp_path_factory.mktemp(f"concurrent_{project_id}")
            
            context = {
                "create_github_repo": False,
                "package_name": f"concurrent_test_{project_id}",
            }
            
            start_time = time.time()
            
            project_path = bake(
                template=str(template_root),
                no_input=True,
                extra_context=context,
                output_dir=tmp_path,
            )
            
            generation_time = time.time() - start_time
            
            # Verify project was created
            assert Path(project_path).exists()
            
            return project_id, generation_time
        
        # Generate 3 projects concurrently
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            start_time = time.time()
            
            futures = [executor.submit(generate_project, i) for i in range(3)]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
            
            total_time = time.time() - start_time
        
        # Check that concurrent generation completed in reasonable time
        # Should be much faster than 3x sequential generation
        assert total_time < 90, f"Concurrent generation took {total_time:.2f}s, which is too slow"
        
        # Verify all projects were created
        assert len(results) == 3
        
        individual_times = [result[1] for result in results]
        print(f"Concurrent generation total time: {total_time:.2f}s")
        print(f"Individual times: {[f'{t:.2f}s' for t in individual_times]}")

    def test_disk_space_efficiency(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test that generated projects don't use excessive disk space."""
        def get_directory_size(path: Path) -> int:
            """Get total size of directory in bytes."""
            total = 0
            for file_path in path.rglob('*'):
                if file_path.is_file():
                    total += file_path.stat().st_size
            return total
        
        project_size = get_directory_size(generated_template_path)
        project_size_mb = project_size / 1024 / 1024
        
        # Generated project should be under 50MB (including .venv and .git)
        assert project_size_mb < 50, f"Generated project size is {project_size_mb:.2f}MB, which is too large"
        
        print(f"Generated project size: {project_size_mb:.2f} MB")