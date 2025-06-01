#!/usr/bin/env python3
import sys


def pre_generation_tasks() -> int:
    """Things to do before cookiecutter renders the template."""
    return 0


if __name__ == "__main__":
    sys.exit(pre_generation_tasks())
