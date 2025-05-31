#!/usr/bin/env python3

import shlex
import subprocess
import sys


def post_generation_tasks() -> int:

    tasks = [
        (True, "uv --verbose venv"),
        (False, "direnv allow"),
        (True, "uv --quiet --no-progress sync"),
        (True, "git init --quiet --initial-branch main"),
    ]

    for is_required, task in tasks:
        try:
            print(f"Post Task [{task}]: ", end="", flush=True)
            results = subprocess.run(shlex.split(task), check=True, capture_output=True)
            print("succeeded.")
        except Exception as error:
            print(f"failed: {error}")
            if is_required:
                return -1
    return 0


if __name__ == "__main__":
    sys.exit(post_generation_tasks())
