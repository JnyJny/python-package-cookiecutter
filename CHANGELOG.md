# CHANGELOG

## [v1.7.10](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/v1.7.10) - 2025-07-13 19:23:26

## Changes since v1.7.9

- v1.7.10 (18d16af)
- Updated tests (fd26a73)
## Full Changelog

See [CHANGELOG.md](CHANGELOG.md) for complete release notes.


**Full Changelog**: https://github.com/JnyJny/python-package-cookiecutter/compare/v1.7.9...v1.7.10

## [v1.7.5](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/v1.7.5) - 2025-07-12 16:18:35

## Changes since v1.7.4

- v1.7.5 (0d37899)
- Updated test suite (4bde2cd)
- Updated pyproject.toml (bd7b5f8)
- Removed no-license license (924b30a)
- Revert Dependabot auto-merge implementation (fe119f8)
- Implement Dependabot auto-merge for safe dependency updates (ebed502)
- Update documentation to reflect current workflow and command structure (4e6d58b)
- Rename github-release.yml to release.yaml to fix README badge (09239c5)
## Full Changelog

See [CHANGELOG.md](CHANGELOG.md) for complete release notes.


**Full Changelog**: https://github.com/JnyJny/python-package-cookiecutter/compare/v1.7.4...v1.7.5

## [v1.7.4](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/v1.7.4) - 2025-07-11 22:14:44

## Changes since v1.7.3

- v1.7.4 (8faeca0)
- Fix Python version in GitHub release workflow (2f00fd7)
## Full Changelog

See [CHANGELOG.md](CHANGELOG.md) for complete release notes.


**Full Changelog**: https://github.com/JnyJny/python-package-cookiecutter/compare/v1.7.3...v1.7.4

## [v1.7.2](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/v1.7.2) - 2025-07-09 20:46:59

I asked Claude to:
- improve test coverage
- add MkDocs integration
- other stuff

That guy is a total chad. 

## [v1.6.0](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/v1.6.0) - 2025-07-04 21:21:13

It turns out some things were broken and now we can test for them.

- Testing: Added better option testing.
- Bug: Picking some licenses was not possible.
- Feature: User can choose to use hatchling or uv for the backend build system.

The uv build backend was recently declared stable and is stupidly fast. I think we're going to have to come up with a better way to describe fast things, perhaps it's _uv fast_. 

## [v1.5.1](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/v1.5.1) - 2025-06-22 22:26:40

Like Fight Club, the first rule of Programming Club is never tell anyone about your code. I broke that rule and got some great feedback.
- MIT License not offered although metadata was present (fixed).
- Added an option for no license.
- User can opt to make their GitHub repo private.
- If `gh` is not found, prompts related to GitHub are removed.
- Updates to pyproject to improve ruff rules (commented rules)

## [v1.4.0](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/v1.4.0) - 2025-06-21 23:03:15

I re-wrote the cookiecutter hooks so they would emit better errors when there were problems.
 - Removed Task from post_gen_project.py
 - Renamed hook files:
   - pre_prompt.py -> pre_prompt.uv
   - pre_gen_project.py -> pre_gen_project.uv
   - post_gen_project.py -> post_gen_project.uv
 - Added uv shebang magic to hooks.
 - Added inline script metadata to add dependencies
 - Call commands using `sh` module
 - Customized the logger from loguru
 - Added logging for optional and required events.
 - Added a README to explain further.
    

## [v1.3.1](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/v1.3.1) - 2025-06-20 18:22:40

For this release, I concentrated on getting all the source to pass ruff check and format cleanly:
- cookiecutter hooks
- cookiecutter tests
- template src
- template tests

## [1.3.1](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/1.3.1) - 2025-06-16 21:29:25

I accidentally left a broken trailing comma in cookiecutter.json. It's fixed now.

## [v1.3.0](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/v1.3.0) - 2025-06-16 00:00:27

This release features more quality of life changes with respect to defaults and optional features.
- dependabot configured by default.
- OS and Python version test matrices are now configurable.
- Added a prompt to specify development Python version
- Added post generation task to install dev Python if necessary
- Virtual environment creation honors dev Python version choice.

## [v1.2.0](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/v1.2.0) - 2025-06-14 18:38:59

This release features:
- **python-package-cookiecutter** license switch from MIT to Apache-2.0.
- tons of GitHub quality-of-life additions to the generated project:
   - Issue templates.
   - Pull request template.
   - CONTRIBUTING.md skeleton.
   - Support for choosing any licenses available via `gh repo license list`.
   - dependabot checking for updated project dependencies and actions.
-  Project cli includes a sub-command `self` scaffold.
-  Updated project pyproject.toml with more good stuff.
-  Fixed some broken indention due to Jinja whitespace magic. 

## [v1.0.1](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/v1.0.1) - 2025-06-03 20:41:38

Cleaned up spelling errors, added extended prompt text, refactored the hooks a little. Mostly small fixes and changes gleaned from looking at other cookiecutter templates. 

## [v1.0.0](https://github.com/JnyJny/python-package-cookiecutter/releases/tag/v1.0.0) - 2025-06-02 01:12:08

This marks the first feature complete usable state of this cookiecutter template.

**Full Changelog**: https://github.com/JnyJny/python-package-cookiecutter/commits/v1.0.0

\* *This CHANGELOG was automatically generated by [auto-generate-changelog](https://github.com/BobAnkh/auto-generate-changelog)*
