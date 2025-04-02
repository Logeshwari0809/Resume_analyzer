#!/bin/bash

# Install the spaCy model
python -m spacy download en_core_web_sm

# Start the FastAPI server using Gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:10000
