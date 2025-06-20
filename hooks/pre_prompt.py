#!/usr/bin/env python
"""Pre-prompt tasks for cookiecutter templates."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from cookiecutter.config import logger
from post_gen_project import Task
from typing import NamedTuple


class Version(NamedTuple):
    major: str
    minor: str
    patch: str

    def __str__(self) -> str:
        """Return the version as a string."""
        return f"{self.major}.{self.minor}"

    def __lt__(self, other: Version) -> bool:
        """Compare two Version instances."""
        if self.major == other.major:
            return self.minor < other.minor
        return self.major < other.major

    def __eq__(self, other: Version) -> bool:
        """Check if two Version instances are equal."""
        return self.major == other.major and self.minor == other.minor

    def __hash__(self) -> int:
        """Return a hash of the version."""
        return hash((self.major, self.minor))


def available_python_versions() -> list[str]:
    """Returns a list of available Python versions, sorted least to greatest."""

    task = Task(
        "Available Python Versions",
        "uv python list --output-format json",
        required=False,
    )
    try:
        results = json.loads(task(verbose=False))
    except Exception as error:
        logger.error(f"Failed to get available Python versions: {error}")
        return []

    available = set()
    for item in results:
        if "b" in item["version"]:
            continue
        available.add(Version(**item["version_parts"]))

    return [str(v) for v in sorted(available)]


def pre_prompt_tasks(config_file: str | Path | None = None) -> int:
    """Things to do before prompting the user."""
    config_file = Path(config_file or "cookiecutter.json")

    tasks = [
        (
            "github_username",
            Task(
                "GitHub Username",
                "git config --global user.name",
                required=False,
            ),
        ),
        (
            "email",
            Task(
                "GitHub Email",
                "git config --global user.email",
                required=False,
            ),
        ),
    ]

    try:
        cookiecutter = json.load(config_file.open())

        for key, task in tasks:
            result = task(verbose=False)
            if result:
                cookiecutter[key] = result

        cookiecutter["_python_versions"] = available_python_versions()

        json.dump(cookiecutter, config_file.open("w"), indent=4)

    except Exception as error:
        logger.warn(f"Pre-Prompt Tasks failed: {error}")
        raise

    return 0


if __name__ == "__main__":
    sys.exit(pre_prompt_tasks())
