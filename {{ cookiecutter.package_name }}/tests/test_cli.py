"""test CLI"""

from typer.testing import CliRunner

from thing.__main__ import cli

runner = CliRunner()


def test_cli_no_arguments() -> None:
    """Test the main command-line interface with no arguments."""
    result = runner.invoke(cli)
    assert result.exit_code != 0
    assert "Usage:" in result.output


def test_cli_help() -> None:
    """Test the main command-line interface help flag."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0


def test_cli_self_no_arguments() -> None:
    """Test the self subcommand with no arguments."""
    result = runner.invoke(cli, ["self"])
    assert result.exit_code != 0
    assert "Usage:" in result.output


def test_cli_self_help() -> None:
    """Test the self subcommand help flag"""
    result = runner.invoke(cli, ["self", "--help"])
    assert result.exit_code == 0


def test_cli_self_version(project_version: str) -> None:
    """Test the version self subcommand."""
    result = runner.invoke(cli, ["self", "version"])
    assert result.exit_code == 0
    assert result.output.strip() == project_version
