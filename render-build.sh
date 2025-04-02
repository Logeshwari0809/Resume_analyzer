#!/bin/bash

# Install the spaCy model
python -m spacy download en_core_web_sm

# Run FastAPI server
uvicorn main:app --host 0.0.0.0 --port $PORT
