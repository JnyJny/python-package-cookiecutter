"""{{ cookiecutter.package_name }}.

{{cookiecutter.project_short_description.rstrip()}}{% if cookiecutter.project_short_description.rstrip() and cookiecutter.project_short_description.rstrip()[-1] not in '.!?:;' %}.{% endif %}
"""

from loguru import logger

logger.disable("{{ cookiecutter.package_name }}")
