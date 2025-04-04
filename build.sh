#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install --no-cache-dir -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
