#!/usr/bin/env python3

import shlex
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple

_SUCCESS = "🟢"
_FAILED_NOTREQUIRED = "🟡"
_FAILURE = "🔴"


class Task(NamedTuple):
    name: str
    task: str
    required: bool

    def __str__(self) -> str:
        return f"Task [{self.name.ljust(30, '.')}]"

    @property
    def cmd(self) -> list[str]:
        return shlex.split(self.task)

    def __call__(self, verbose: bool = True) -> str:
        try:
            results = subprocess.run(
                self.cmd,
                check=True,
                capture_output=True,
                universal_newlines=True,
                shell=False,
            )
            if verbose:
                print(self, _SUCCESS)
            return results.stdout.strip()
        except subprocess.CalledProcessError as error:
            if not self.required:
                print(self, _FAILED_NOTREQUIRED)
            else:
                print(self, _FAILURE)
                print(f"\tCommand: {self.task}")
                print(f"\tstdout:  {error.stdout}")
                print(f"\tstderr:  {error.stderr}")

                raise

            return ""


def post_generation_tasks() -> int:
    """Things to do after cookiecutter has rendered the template."""

    tasks = [
        Task("Create .venv", "uv --verbose venv", required=True),
        Task("Enable Direnv", "direnv allow", required=False),
        Task("Sync Project Deps", "uv --quiet --no-progress sync", required=True),
        Task("Initialize Git", "git init --quiet --initial-branch main", required=True),
        Task("Add Files", "git add .", required=True),
        Task("Initial Commit", "git commit -m 'initial commit'", required=True),
    ]

    if "{{ cookiecutter.create_github_repo }}".lower() == "yes":
        create_repo = Task(
            "Create Upstream Repo",
            f"gh repo create {{ cookiecutter.package_name }} --public --push --source=. --remote=upstream",
            required=False,
        )
        tasks.append(create_repo)

    try:
        for task in tasks:
            task()
        return 0
    except Exception as error:
        print(f"{task} {task.task} {error}")
        return -1


if __name__ == "__main__":
    sys.exit(post_generation_tasks())
