"""test cookiecutter.json."""

import json
from pathlib import Path


def test_cookiecutter_json_valid(cookiecutter_json_path: Path) -> None:
    """Checks that cookiecutter.json exists and is valid JSON."""
    assert cookiecutter_json_path.exists()
    assert cookiecutter_json_path.is_file()
    assert json.load(cookiecutter_json_path.open())
