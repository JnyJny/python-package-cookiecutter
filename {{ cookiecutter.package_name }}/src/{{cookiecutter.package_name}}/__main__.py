"""{{ cookiecutter.cli_name }} 

{{ cookiecutter.project_short_description }}
"""

import sys

import typer
from loguru import logger

from .self_subcommand import cli as self_cli
{%- if cookiecutter.use_pydantic_settings %}
from .settings import Settings
{%- endif %}

cli = typer.Typer()

cli.add_typer(
    self_cli,
    name="self",
    help="Manage the {{ cookiecutter.cli_name }} command.",
)


@cli.callback(invoke_without_command=True, no_args_is_help=True)
def global_callback(
    ctx: typer.Context,
    debug: bool = typer.Option(False, "--debug", "-D", help="Enable debugging output."),
) -> None:
    """{{ cookiecutter.project_short_description }}"""
{%- if cookiecutter.use_pydantic_settings %}
    ctx.obj = Settings()
    debug = debug or ctx.obj.debug
{%- endif %}
    (logger.enable if debug else logger.disable)("{{ cookiecutter.package_name }}")
{%- if cookiecutter.log_to_file %}
    logger.add("{{ cookiecutter.package_name }}.log")
{%- endif %}
    logger.info(f"{debug=}")


if __name__ == "__main__":
    sys.exit(cli())
