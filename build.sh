#!/bin/bash

# Exit immediately if any command fails
set -e

echo "Creating virtual environment..."
python -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Downloading spaCy model..."
python -m spacy download en_core_web_sm

echo "Build completed successfully!"
