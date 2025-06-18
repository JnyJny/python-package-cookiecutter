""" """

import pytest
from pathlib import Path
import json


@pytest.fixture(scope="session")
def cookiecutter_path() -> Path:
    yield Path("../cookiecutter.json")


@pytest.fixture()
def cookiecutter_contents(cookiecutter_path: Path) -> dict:
    yield json.load(cookiecutter_path.open())
