#!/usr/bin/env python3
"""Post generation tasks for cookiecutter templates."""

import shlex
import subprocess
import sys
from typing import NamedTuple

_SUCCESS = "🟢"
_FAILED_NOTREQUIRED = "🟡"
_FAILURE = "🔴"


class Task(NamedTuple):
    """A cookiecutter generation task."""

    name: str
    task: str
    required: bool

    def __str__(self) -> str:
        """Render the task as a string."""
        return f"Task [{self.name.ljust(30, '.')}]"

    @property
    def cmd(self) -> list[str]:
        """Return the command to run as a lexically safe list."""
        return shlex.split(self.task)

    def __call__(self, *, verbose: bool = True) -> str:
        """Run the task and return the output."""
        try:
            results = subprocess.run(  # noqa: S603
                self.cmd,
                check=True,
                capture_output=True,
                text=True,
                shell=False,
            )
            if verbose:
                print(self, _SUCCESS)  # noqa: T201
            return results.stdout.strip()
        except subprocess.CalledProcessError as error:
            if not self.required:
                print(self, _FAILED_NOTREQUIRED, error)  # noqa: T201
            else:
                print(self, _FAILURE)  # noqa: T201
                print(f"\tCommand: {self.task}")  # noqa: T201
                print(f"\tstdout:  {error.stdout}")  # noqa: T201
                print(f"\tstderr:  {error.stderr}")  # noqa: T201

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
            "gh repo create {{ cookiecutter.package_name }} --public"
            " --push --source=. --remote=upstream",
            required=False,
        )
        tasks.append(create_repo)

    try:
        for task in tasks:
            task()
    except Exception as error:
        print(f"{task} {task.task} {error}")  # noqa: T201
        raise

    return 0


if __name__ == "__main__":
    sys.exit(post_generation_tasks())
