#!/usr/bin/env python3
"""Post generation tasks for cookiecutter templates."""

import shlex
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from typing import NamedTuple

from cookiecutter.config import logger

_SUCCESS = "🟢"
_FAILED_NOTREQUIRED = "🟡"
_FAILURE = "🔴"


class Task(NamedTuple):
    """A cookiecutter hook task."""

    name: str
    task: str | Callable[[], str]
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
        except FileNotFoundError as error:
            if self.required:
                raise
            logger.error(self, _FAILED_NOTREQUIRED, error)

        except subprocess.CalledProcessError as error:
            if self.required:
                print(self, _FAILURE, error)  # noqa: T201
                logger.error("\tCommand: %s", self.task)
                logger.error("\t stdout: %s", error.stdout)
                logger.error("\t stderr: %s", error.stderr)
                raise

            print(self, _FAILED_NOTREQUIRED, error)  # noqa: T201

        return ""


uv_venv_cmd = """
uv venv --python {{ cookiecutter.python_version_dev }} --managed-python
""".strip()


def remove_empty_comments(path: Path | str) -> None:
    """Remove empty comments from Python files in the given path."""
    path = Path(path)

    for pypath in path.rglob("*.py"):
        lines = pypath.read_text().splitlines()
        text = [line for line in lines if line.strip() != "#"]
        pypath.write_text("\n".join(text) + "\n")


def post_generation_tasks() -> int:
    """Things to do after cookiecutter has rendered the template."""
    tasks = [
        Task(
            "Install Dev Python",
            "uv python install {{ cookiecutter.python_version_dev }}",
            required=True,
        ),
        Task("Create .venv", uv_venv_cmd, required=True),
        Task("Enable Direnv", "direnv allow", required=False),
        Task("Sync Project Deps", "uv --quiet --no-progress sync", required=True),
        Task("Ruff Check Source", "uvx ruff check --fix src tests", required=True),
        Task("Initialize Git", "git init --quiet --initial-branch main", required=True),
        Task("Add Files", "git add .", required=True),
        Task("Initial Commit", "git commit -m 'initial commit'", required=True),
    ]

    create_github_repo = "{{ cookiecutter.create_github_repo }}"

    if create_github_repo == "True":
        create_repo = Task(
            f"Create Upstream Repo {create_github_repo}",
            "gh repo create {{ cookiecutter.package_name }} --public"
            " --push --source=. --remote=upstream",
            required=False,
        )
        tasks.append(create_repo)

    for pysrc in ["src", "tests"]:
        remove_empty_comments(pysrc)

    try:
        for task in tasks:
            task()
    except Exception as error:
        print(f"{task} {task.task} {error}")  # noqa: T201
        raise

    return 0


if __name__ == "__main__":
    sys.exit(post_generation_tasks())
