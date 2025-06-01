#!/usr/bin/env python

import json
import os
import sys
from datetime import datetime
from pathlib import Path

from post_gen_project import Task


def pre_prompt_tasks(config_file: str | Path = None) -> int:
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

        cookiecutter["year"] = datetime.now().year

        for key, task in tasks:
            try:
                cookiecutter[key] = task(verbose=False)
            except:
                pass

        json.dump(cookiecutter, config_file.open("w"), indent=4)
    except Exception as error:
        print(f"Pre-Prompt Tasks failed: {error}")
        return -1
    return 0


if __name__ == "__main__":
    sys.exit(pre_prompt_tasks())
