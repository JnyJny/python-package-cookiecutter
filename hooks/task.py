""" """

import shlex
import subprocess
from typing import NamedTuple


class Task(NamedTuple):
    task: str
    required: bool

    @property
    def cmd(self) -> list[str]:
        return shlex.split(self.task)

    def __call__(self, prefix: str = None, verbose: bool = False) -> str:

        prefix = prefix + " " if prefix else ""

        try:
            if verbose:
                print(f"{prefix}Task [{self.task}]: ", end="", flush=True)
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
                raise
            return ""
