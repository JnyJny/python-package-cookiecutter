"""Test that poe tasks work correctly in generated projects."""

import subprocess
from pathlib import Path

import pytest


def test_poe_tasks_exist(generated_template_path: Path) -> None:
    """Test that all expected poe tasks are defined in generated project."""
    pyproject_path = generated_template_path / "pyproject.toml"
    assert pyproject_path.exists()
    
    content = pyproject_path.read_text()
    expected_tasks = [
        "coverage", "mypy", "ty", "ruff-check", "ruff-format", "ruff", 
        "check", "test", "qc", "publish_patch", "publish_minor", 
        "publish_major", "publish", "clean", "tree"
    ]
    
    for task in expected_tasks:
        assert f"{task}." in content or f"{task} =" in content, f"Task {task} not found in pyproject.toml"


def test_poe_tasks_execute(generated_template_path: Path) -> None:
    """Test that key poe tasks execute without errors in generated project."""
    # Tasks that should work without additional setup
    safe_tasks = ["tree", "clean"]
    
    for task in safe_tasks:
        result = subprocess.run(
            ["uv", "run", "poe", task],
            cwd=generated_template_path,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0, f"Task '{task}' failed: {result.stderr}"


def test_poe_test_task(generated_template_path: Path) -> None:
    """Test that the poe test task works in generated project."""
    result = subprocess.run(
        ["uv", "run", "poe", "test"],
        cwd=generated_template_path,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"poe test failed: {result.stderr}"
    assert "passed" in result.stdout, "Tests should pass in generated project"


def test_poe_ruff_tasks(generated_template_path: Path) -> None:
    """Test that ruff tasks work in generated project."""
    for task in ["ruff-check", "ruff-format", "ruff"]:
        result = subprocess.run(
            ["uv", "run", "poe", task],
            cwd=generated_template_path,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0, f"Task '{task}' failed: {result.stderr}"


def test_poe_type_checking_tasks(generated_template_path: Path) -> None:
    """Test that type checking tasks work in generated project."""
    for task in ["mypy", "ty"]:
        result = subprocess.run(
            ["uv", "run", "poe", task],
            cwd=generated_template_path,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0, f"Task '{task}' failed: {result.stderr}"


def test_poe_check_task(generated_template_path: Path) -> None:
    """Test that the comprehensive check task works."""
    result = subprocess.run(
        ["uv", "run", "poe", "check"],
        cwd=generated_template_path,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"poe check failed: {result.stderr}"


@pytest.mark.slow
def test_poe_qc_task(generated_template_path: Path) -> None:
    """Test that the quality control task works (marked as slow)."""
    result = subprocess.run(
        ["uv", "run", "poe", "qc"],
        cwd=generated_template_path,
        capture_output=True,
        text=True,
        timeout=120  # 2 minutes timeout
    )
    assert result.returncode == 0, f"poe qc failed: {result.stderr}"