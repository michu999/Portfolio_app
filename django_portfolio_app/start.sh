#!/bin/bash

# Set the Python path to include your project
export PYTHONPATH=$PYTHONPATH:/app

# Start Gunicorn with the PORT environment variable that Render provides
gunicorn portfolio_app.wsgi:application --bind 0.0.0.0:$PORT