#!/bin/bash

# Exit if any command fails
set -e

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Downloading spaCy model..."
python -m spacy download en_core_web_sm

echo "Starting the application..."
uvicorn main:app --host 0.0.0.0 --port $PORT
