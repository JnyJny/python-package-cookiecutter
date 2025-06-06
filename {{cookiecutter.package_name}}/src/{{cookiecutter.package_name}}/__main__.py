""" {{ cookiecutter.package_name }}

{{ cookiecutter.project_short_description }}
"""

import sys

import typer
from loguru import logger

{%- if cookiecutter.use_pydantic_settings == "yes" %}
from .settings import {{ cookiecutter.package_name.title() }}Settings
{%- endif %}

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
{%- if cookiecutter.use_pydantic_settings == "yes" %}
     ctx.obj = {{ cookiecutter.package_name.title() }}Settings()
    debug = debug or ctx.obj.debug
{%- endif %}
    (logger.enable if debug else logger.disable)("{{ cookiecutter.package_name }}")
{%- if cookiecutter.log_to_file == "yes" %}
    logger.add("{{ cookiecutter.package_name }}.log")
{% endif -%}    
    logger.info(f"{debug=}")


if __name__ == "__main__":
    sys.exit(cli())
