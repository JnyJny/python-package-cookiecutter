# UV Hooks

Cookiecutter looks for three files to run during the templating process:
1. `pre_prompt`
1. `pre_gen_project`
1. `post_gen_project`

If the file in question has a `.py` suffix, it attempts to run using
Python otherwise it execs the file with `subprocess`.

It's nice to write the hooks in Python, however the execution
environment for the hooks is kinds of ambiguous and limits the
hook implementations to only using the Python standard library.

So I did a thing.

The files in this directory have a suffix `.uv` indicating that they
are **not** Python programs, so cookiecutter execs them using
`subprocess`. This lets me run the code in the file using uv to 
satisfy dependencies without relying on the execution environment
to supply them.

### `pre_prompt.uv`

```python
#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.13"
# dependencies = [ "sh", "packaging>=25", "loguru" ]
# ///
...
```

## Justification for this Hackery?

I wanted to use `loguru` for logging and `sh` for command execution.


