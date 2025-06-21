#!/bin/bash
pip install --upgrade pip
pip install wheel setuptools
pip install --only-binary :all: -r requirements.txt
