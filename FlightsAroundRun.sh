#!/bin/bash

if [[ -d ".venv" ]]; then
    .venv/bin/python3 main.py &
else
    echo "Error, this script is meant to run vith venv, which has not been found"
    fi