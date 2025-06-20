"""test {{ cookiecutter.package_name }} CLI: {{ cookiecutter.cli_name }}."""

from typer.testing import CliRunner
import importlib

main_module_name = "{{ cookiecutter.package_name }}.__main__"
main_module = importlib.import_module(main_module_name)
runner = CliRunner()


def test_cli_no_arguments() -> None:
    """Test the main command-line interface with no arguments."""
    result = runner.invoke(main_module.cli)
    assert result.exit_code != 0
    assert "Usage:" in result.output


def test_cli_help() -> None:
    """Test the main command-line interface help flag."""
    result = runner.invoke(main_module.cli, ["--help"])
    assert result.exit_code == 0


def test_cli_self_no_arguments() -> None:
    """Test the self subcommand with no arguments."""
    result = runner.invoke(main_module.cli, ["self"])
    assert result.exit_code != 0
    assert "Usage:" in result.output


def test_cli_self_help() -> None:
    """Test the self subcommand help flag."""
    result = runner.invoke(main_module.cli, ["self", "--help"])
    assert result.exit_code == 0


def test_cli_self_version(project_version: str) -> None:
    """Test the version self subcommand."""
    result = runner.invoke(main_module.cli, ["self", "version"])
    assert result.exit_code == 0
    assert result.output.strip() == project_version
