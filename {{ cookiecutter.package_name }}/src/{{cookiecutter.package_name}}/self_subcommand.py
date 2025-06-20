"""{{ cookiecutter.cli_name }} Self Command-Line Interface.

This module provides a command-line interface to interact with
internals of the {{ cookiecutter.cli_name }} CLI.
"""

from importlib.metadata import version

import typer
from loguru import logger

cli = typer.Typer()


@cli.command(name="version")
def version_subcommand() -> None:
    """Retrieve the package version."""
    try:
        pkg_version = version("{{ cookiecutter.package_name }}")
        logger.info(f"Package version: {pkg_version}")
        typer.secho(pkg_version, fg=typer.colors.GREEN)
    except Exception as error:
        logger.error(f"Failed to retrieve package version: {error}")
        raise typer.Exit(code=1) from None
