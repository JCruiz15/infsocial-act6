#!/bin/bash

# Create Python virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install requirements
pip install --no-cache-dir -r requirements.txt

# Run the application

python3 main.py