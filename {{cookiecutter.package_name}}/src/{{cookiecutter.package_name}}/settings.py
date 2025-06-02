"""
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class {{ cookiecutter.package_name.title() }}Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="{{ cookiecutter.package_name.upper() }}",
        env_file=".env-{{ cookiecutter.package_name.lower() }}",
    )
    debug: bool  = False
