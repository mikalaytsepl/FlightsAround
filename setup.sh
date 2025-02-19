#!/bin/bash

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))' 2>/dev/null)

# if python version in empty it means that python is not installed 
if [[ -z "$PYTHON_VERSION" ]]; then
    echo "Python3 is not installed. Please install Python >= 3.11."
    exit 1
fi


REQUIRED_VERSION="3.11"

# sorting the installed version with the required and if it appears last it means that other versions are >= then required
if [[ "$(printf "%s\n%s" "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]]; then
    echo "Python >= 3.11 is required. Found version: $PYTHON_VERSION"
    exit 1
fi

echo "Python version is sufficient: $PYTHON_VERSION"

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements

echo "Setup complete. Virtual environment activated.\n You can run it with .sh script or manually using correct interpreter and main.py"