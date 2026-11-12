# sequence

A Python package for numerical sequences.

This is an example repository for the course
[Open Source Software Development for Astronomy](https://github.com/prashjet/oss4astro-course)
at the University of Vienna.

## Installation and use

From a clone, in your own Python environment:

```sh
pip install .
python -c "from sequence import even; print(even(10))"
```

## Development

Install [uv](https://docs.astral.sh/uv/getting-started/installation/),
then, from your clone, run:

```sh
uv sync --locked
```

This installs the package in editable mode, along with its runtime
and development dependencies. Changes to files in `src/sequence/`
take effect without reinstalling.

To try your changes:

```sh
uv run python -c "from sequence import even; print(even(10))"
```
