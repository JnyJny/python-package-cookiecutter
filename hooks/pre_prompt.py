#!/usr/bin/env python

import json
import os
import shlex
import subprocess
import sys
from functools import cached_property
from pathlib import Path

config_json = Path("cookiecutter.json")


class Identity:
    def __init__(self) -> None:
        pass

    def git_config(self, item: str, scope: str = "--global") -> str:
        results = subprocess.run(
            shlex.split(f"git config {scope} {item}"),
            capture_output=True,
            check=True,
            universal_newlines=True,
        )
        return results.stdout.strip()

    @cached_property
    def name(self) -> str:
        try:
            return self.git_config("user.name")
        except:
            return os.environ.get("USER", "unknown_user")

    @cached_property
    def email(self) -> str:
        try:
            return self.git_config("user.email")
        except:
            return os.environ.get("EMAIL", "unknown_email")

    def as_dict(self) -> dict[str, str]:
        return {"github_username": self.name, "email": self.email}


def pre_prompt_tasks() -> int:

    identity = Identity()

    config = json.load(config_json.open())

    try:
        config |= identity.as_dict()
        json.dump(config, config_json.open("w"))
    except Exception as error:
        print(f"Pre Prompt Tasks failed: {error}")
        return -1

    return 0


if __name__ == "__main__":
    sys.exit(pre_prompt_tasks())
