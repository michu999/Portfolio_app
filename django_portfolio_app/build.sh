#!/bin/bash
# Set environment variable
export RENDER=true

# Add the current directory to the Python path
export PYTHONPATH=$PYTHONPATH:/opt/render/project/src

# Start Gunicorn
cd /opt/render/project/src
exec gunicorn portfolio_app.wsgi:application