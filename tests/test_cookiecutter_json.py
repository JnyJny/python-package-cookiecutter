"""test cookiecutter.json for correctness."""

import json
from pathlib import Path


def test_cookiecutter_json_valid(cookiecutter_json_path: Path) -> None:
    """Checks that cookiecutter.json exists and is valid JSON."""
    assert cookiecutter_json_path.exists()
    assert cookiecutter_json_path.is_file()
    result = json.load(cookiecutter_json_path.open())
    assert isinstance(result, dict), "cookiecutter.json should be a dictionary"
