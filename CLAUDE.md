# CLAUDE.md

Cookiecutter template for modern Python packages with CLI, testing, and GitHub automation.

## Commands

**Testing**: `pytest` (103 tests, 5-15m) | `poe test_fast` (26 tests, 35s) | `poe ruff`  
**Development**: `poe bake` (test project) | `poe clean` (cleanup) | `uv sync`  
**Release**: `poe release_patch/minor/major` (template) | `poe publish_patch/minor/major` (generated projects)

## Structure

**Template**: `cookiecutter.json` (config) | `hooks/` (setup scripts) | `{{ cookiecutter.package_name }}/` (template) | `tests/`  
**Generated**: `src/` layout | Typer CLI | pydantic-settings | Loguru | poe tasks | GitHub automation  
**Hooks**: Auto-install Python, create venv, sync deps, init git, optional GitHub repo

## GitHub Workflows

**Generated Projects**: `release.yaml` (test, build, PyPI, docs) | `docs.yml` (GitHub Pages) | `dependabot.yaml`  
**Template Repo**: `release.yaml` (test, GitHub releases, no PyPI)  
**Features**: Dynamic Python versions, auto-changelog, trusted publishing, repository dispatch

## Testing

**Coverage**: Config validation | Project generation | CLI integration | Build/packaging | Cross-platform | Workflows  
**Infrastructure**: Parametrized tests | Subprocess validation | Fast subset (26 tests) | Full suite (103 tests)

## Workflows

**Template Changes**: Modify `{{ cookiecutter.package_name }}/` → Add tests → `poe bake` → `poe ruff`  
**Dependencies**: Update both root and template `pyproject.toml`  
**GitHub Testing**: `poe bake` → Test workflows in generated project → Validate with different configs

## Releases

**Template**: `poe release_patch/minor/major` → Auto-test + GitHub release (no PyPI)  
**Generated Projects**: `poe publish_patch/minor/major` → Auto-test + PyPI + GitHub release + docs

Dynamic Python version config: `[tool.package.ci] test-python-versions = ["3.11", "3.12"]`