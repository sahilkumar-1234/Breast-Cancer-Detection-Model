#!/bin/bash
# Install system dependencies first
pip install --upgrade pip
pip install wheel setuptools==65.5.1

# Install Python packages with explicit flags
pip install --no-cache-dir --only-binary=:all: --use-pep517 -r requirements.txt
