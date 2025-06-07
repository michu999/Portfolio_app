#!/bin/bash

# Set environment variables
export RENDER=true
export PYTHONPATH=$PYTHONPATH:/opt/render/project/src

# Navigate to the correct directory
cd /opt/render/project/src

# Start Gunicorn with the correct WSGI path
exec gunicorn --bind 0.0.0.0:$PORT portfolio_app.wsgi:application