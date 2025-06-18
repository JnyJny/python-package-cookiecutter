"""test cookiecutter.json."""

import json
from pathlib import Path


def test_cookiecutter_json_valid(cookiecutter_path: Path) -> None:
    """Checks that cookiecutter.json is valid JSON."""
    assert json.load(cookiecutter_path.open()), f"Failed to open {cookiecutter_path}"
