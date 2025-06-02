#!/usr/bin/env python3

import shlex
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple


class Task(NamedTuple):
    name: str
    task: str
    required: bool

    @property
    def cmd(self) -> list[str]:
        return shlex.split(self.task)

    def __call__(self, verbose: bool = True) -> str:
        try:
            if verbose:
                print(f"Task [{self.name:20}]: ", end="", flush=True)
            results = subprocess.run(
                self.cmd,
                check=True,
                capture_output=True,
                universal_newlines=True,
            )
            if verbose:
                print("succeeded.")
            return results.stdout.strip()
        except Exception as error:
            if verbose:
                print(f"failed: {error}")

            if self.required:
                print(f"Command: {self.task}")
                print(f"stdout:  {error.stdout}")
                print(f"stderr:  {error.stderr}")
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
            f"gh repo create {{ cookiecutter.package_name }} --private --source=. --remote=upstream",
            required=False,
        )
        push_initial_commit = Task(
            "Push To Upstream",
            "git push --set-upstream upstream main",
            required=False,
        )
        tasks.extend([create_repo, push_initial_commit])

    try:
        for task in tasks:
            task()
        return 0
    except:
        return -1


if __name__ == "__main__":
    sys.exit(post_generation_tasks())
