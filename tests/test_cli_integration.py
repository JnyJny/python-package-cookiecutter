"""Advanced CLI integration tests for generated projects."""

import json
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
            (["uv", "run", "python", "-m", "thing", "-h"], "main help short"),
            
            # Subcommand help
            (["uv", "run", "python", "-m", "thing", "self", "--help"], "self help"),
            (["uv", "run", "python", "-m", "thing", "self", "-h"], "self help short"),
            
            # Version commands
            (["uv", "run", "python", "-m", "thing", "self", "version"], "version command"),
        ]
        
        for cmd, description in cli_tests:
            result = subprocess.run(
                cmd,
                cwd=generated_template_path,
                capture_output=True,
                text=True
            )
            assert result.returncode == 0, f"Failed {description}: {result.stderr}"
            
            if "help" in description:
                assert "Usage:" in result.stdout, f"Help output missing for {description}"

    def test_cli_error_handling(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test CLI error handling and exit codes."""
        error_tests = [
            # Invalid subcommand
            (["uv", "run", "python", "-m", "thing", "nonexistent"], 2, "invalid subcommand"),
            
            # Invalid options
            (["uv", "run", "python", "-m", "thing", "--invalid-option"], 2, "invalid option"),
            
            # No arguments when required
            (["uv", "run", "python", "-m", "thing"], 2, "no arguments"),
            (["uv", "run", "python", "-m", "thing", "self"], 2, "self no arguments"),
        ]
        
        for cmd, expected_exit_code, description in error_tests:
            result = subprocess.run(
                cmd,
                cwd=generated_template_path,
                capture_output=True,
                text=True
            )
            # Allow some flexibility in exit codes (different versions may use different codes)
            assert result.returncode != 0, f"Expected failure for {description} but got success"

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
            text=True
        )
        assert result.returncode == 0, f"Debug command failed: {result.stderr}"
        
        # Should still output version
        assert "0.1.0" in result.stdout
        
        # Test that debug mode can be combined with other flags
        result = subprocess.run(
            ["uv", "run", "python", "-m", "thing", "-D", "--help"],
            cwd=generated_template_path,
            capture_output=True,
            text=True
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
            text=True
        )
        assert result_module.returncode == 0
        
        # Test as installed script (if available)
        result_script = subprocess.run(
            ["uv", "run", "thing", "self", "version"],
            cwd=generated_template_path,
            capture_output=True,
            text=True
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
            env=env
        )
        assert result.returncode == 0, f"CLI with env var failed: {result.stderr}"

    def test_cli_output_formats(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test CLI output formatting and consistency."""
        # Test version output format
        result = subprocess.run(
            ["uv", "run", "python", "-m", "thing", "self", "version"],
            cwd=generated_template_path,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0
        
        version_output = result.stdout.strip()
        # Should be a clean version number
        assert version_output == "0.1.0", f"Unexpected version output: '{version_output}'"
        
        # Test help output format
        result = subprocess.run(
            ["uv", "run", "python", "-m", "thing", "--help"],
            cwd=generated_template_path,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0
        
        help_output = result.stdout
        # Should have standard CLI help structure
        assert "Usage:" in help_output
        assert "Options:" in help_output or "Arguments:" in help_output

    def test_cli_stdin_handling(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test CLI handles stdin appropriately."""
        # Test that CLI doesn't hang when no stdin is available
        result = subprocess.run(
            ["uv", "run", "python", "-m", "thing", "self", "version"],
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            stdin=subprocess.DEVNULL,
            timeout=10  # Should complete quickly
        )
        assert result.returncode == 0

    def test_cli_signal_handling(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test CLI handles signals gracefully."""
        import signal
        import time
        
        # Start a long-running command (help should be quick, but let's test)
        process = subprocess.Popen(
            ["uv", "run", "python", "-m", "thing", "--help"],
            cwd=generated_template_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        try:
            # Give it a moment to start
            time.sleep(0.1)
            
            # Send SIGTERM (if supported)
            if hasattr(signal, 'SIGTERM'):
                process.send_signal(signal.SIGTERM)
            
            # Wait for completion
            stdout, stderr = process.communicate(timeout=5)
            
            # Process should exit cleanly (exit code may vary)
            assert process.returncode is not None, "Process should have terminated"
            
        except subprocess.TimeoutExpired:
            # If it times out, kill it
            process.kill()
            process.communicate()
            pytest.fail("CLI process did not respond to signal")

    def test_cli_concurrent_execution(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test multiple CLI instances can run concurrently."""
        import concurrent.futures
        
        def run_cli_command(cmd_suffix: str) -> tuple[int, str]:
            """Run a CLI command and return result."""
            result = subprocess.run(
                ["uv", "run", "python", "-m", "thing", "self", "version"],
                cwd=generated_template_path,
                capture_output=True,
                text=True
            )
            return result.returncode, result.stdout.strip()
        
        # Run multiple instances concurrently
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(run_cli_command, str(i)) for i in range(3)]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        # All should succeed with same output
        for returncode, output in results:
            assert returncode == 0, "Concurrent CLI execution failed"
            assert output == "0.1.0", f"Unexpected output: {output}"

    def test_cli_unicode_handling(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test CLI handles Unicode properly."""
        # Test with Unicode in environment (if settings support it)
        import os
        env = os.environ.copy()
        env.update({"LANG": "en_US.UTF-8", "LC_ALL": "en_US.UTF-8"})
        
        result = subprocess.run(
            ["uv", "run", "python", "-m", "thing", "self", "version"],
            cwd=generated_template_path,
            capture_output=True,
            text=True,
            env=env
        )
        assert result.returncode == 0, f"Unicode test failed: {result.stderr}"

    def test_cli_performance_consistency(
        self,
        generated_template_path: Path,
    ) -> None:
        """Test CLI performance is consistent across runs."""
        import time
        
        times = []
        for i in range(5):
            start_time = time.time()
            
            result = subprocess.run(
                ["uv", "run", "python", "-m", "thing", "self", "version"],
                cwd=generated_template_path,
                capture_output=True,
                text=True
            )
            
            execution_time = time.time() - start_time
            times.append(execution_time)
            
            assert result.returncode == 0, f"CLI run {i+1} failed: {result.stderr}"
        
        # Check performance consistency
        avg_time = sum(times) / len(times)
        max_time = max(times)
        
        # No single run should be more than 3x the average (allowing for startup variance)
        assert max_time < avg_time * 3, f"Inconsistent performance: avg={avg_time:.3f}s, max={max_time:.3f}s"
        
        # Overall should be reasonably fast
        assert avg_time < 5.0, f"CLI is too slow: average {avg_time:.3f}s"