""" {{ cookiecutter.package_name }}

{{ cookiecutter.project_short_description }}
"""

import sys

import typer
from loguru import logger

cli = typer.Typer()

@cli.callback(invoke_without_command=True, no_args_is_help=True)
def global_callback(
        ctx: typer.Context,
        debug: bool = typer.Option(
            False,
            "--debug",
            '-D',
            help="Enable debugging output"),
) -> None:
    """{{ cookiecutter.project_short_description }}
    """
    (logger.enable if debug else logger.disable)("{{ cookiecutter.package_name }}")
    logger.info(f"{debug=}")



if __name__ == "__main__":
    sys.exit(cli())
