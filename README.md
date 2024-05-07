# Trame Bounding Box Widget

This project expose a widget that let you draw bounding boxes and/or interact with them.

## Usage example

The `./examples/` directory gather simple Python scripts using the widget and exposing them as standalone trame applications.

## Virtual Environment setup

```bash
# Create and activate venv
python3.10 -m venv .venv
source .venv/bin/activate

# Install published package
pip install trame-bbox
```

## Running examples

```bash
# Run the scripts
python ./examples/animation.py
python ./examples/edit.py
python ./examples/new_bbox.py
```

## Dev setup

```bash
pip install pre-commit
pre-commit install

pre-commit run --all-files
```