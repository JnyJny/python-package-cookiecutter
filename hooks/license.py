""" """

from pathlib import Path


def pick_license(license: str) -> None:
    """Given a target license, rearrange the deckchairs."""

    try:
        Path(f"LICENSE.{license}").rename("LICENSE")
    except FileNotFoundError:
        raise ValueError(f"Unknown license {license}") from None

    for loser in Path.cwd().glob("LICENSE.*"):
        loser.unlink()
