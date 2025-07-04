""" """

import pytest
from pathlib import Path
import json

from cookiecutter.main import cookiecutter as bake

from .conftest import check_project_contents

cwd = Path.cwd()

contents = json.loads((cwd / "cookiecutter.json").read_text())

EXTRAS = []
for key, value in contents.items():
    if not isinstance(value, list) or key.startswith("_"):
        continue
    for item in value:
        EXTRAS.append({key: item})


@pytest.mark.parametrize("extra", EXTRAS)
def test_generate_project(
    extra: dict[str, str],
    tmp_path_factory: pytest.TempPathFactory,
    template_root: Path,
    cookiecutter_extra_context: dict,
    cookiecutter_package_name: str,
) -> None:
    tmp_path = tmp_path_factory.mktemp("generated_project")

    project_path = bake(
        template=str(template_root),
        no_input=True,
        extra_context=extra | cookiecutter_extra_context,
        output_dir=tmp_path,
    )

    assert check_project_contents(project_path, cookiecutter_package_name)
