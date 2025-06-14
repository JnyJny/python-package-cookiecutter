#!/usr/bin/env python
"""Pre-prompt tasks for cookiecutter templates."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from post_gen_project import Task


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
            cookiecutter[key] = task(verbose=True)

        json.dump(cookiecutter, config_file.open("w"), indent=4)

    except Exception as error:
        print(f"Pre-Prompt Tasks failed: {error}")  # noqa: T201
        raise

    return 0


if __name__ == "__main__":
    sys.exit(pre_prompt_tasks())
