#!/bin/bash

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Downloading spaCy model..."
python -m spacy download en_core_web_sm

echo "Build completed successfully!"
