"""
"""

from importlib.metadata import version

import typer
from loguru import logger

cli = typer.Typer()

@cli.command(name="version")
def version_subcommand() -> None:
    """Show the version of the package."""
    try:
        pkg_version = version("{{ cookiecutter.package_name }}")
        logger.info(f"Package version: {pkg_version}")
        typer.secho(pkg_version, fg=typer.colors.GREEN)
    except Exception as error:
        logger.error(f"Failed to retrieve package version: {error}")
        raise typer.Exit(code=1)
