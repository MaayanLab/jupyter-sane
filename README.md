# Jupyter (Sane)

This is a cli drop-in replacement for jupyter which constructs a temporary environment and jupyter kernel matching what is active in the current environment at call-time. No longer should you have to worry about jupyter's python installation not matching what you install with pip in or out of your environment.

## Installation

```bash
pip install git+https://github.com/maayanlab/jupyter-sane
```

Use with `jupyter-sane [normal jupyter commands]` or alternatively, add an alias in your `.rc`: `alias jupyter=jupyter-sane`.
