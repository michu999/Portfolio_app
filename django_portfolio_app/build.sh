#!/bin/bash
# Set environment variable
export RENDER=true

# Debug - show current working directory
echo "Starting directory: $(pwd)"

# Navigate to project root
cd /opt/render/project/src/django_portfolio_app

# Add the project root to Python path
export PYTHONPATH=$PYTHONPATH:/opt/render/project/src/django_portfolio_app

# Debug - show Python path
echo "PYTHONPATH: $PYTHONPATH"

# Start Gunicorn with the correct WSGI path
exec gunicorn portfolio_app.wsgi:application