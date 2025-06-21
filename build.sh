#!/bin/bash
# Render-specific build script for Python/Flask apps

# 1. Ensure pip is up-to-date
python -m pip install --upgrade pip

# 2. Install binary dependencies (no compilation)
pip install --no-cache-dir \
    --only-binary=:all: \
    --use-pep517 \
    wheel \
    setuptools==65.5.1

# 3. Install requirements with strict binary-only policy
pip install --no-cache-dir \
    --only-binary=:all: \
    -r requirements.txt
