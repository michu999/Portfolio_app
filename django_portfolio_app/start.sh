#!/bin/bash

# Navigate to the correct directory
cd /opt/render/project/src

# Add the current directory to Python path
export PYTHONPATH=$PYTHONPATH:/opt/render/project/src

# Check directory structure (for debugging)
ls -la

# Try to find where your Django project is located
find . -name "wsgi.py" -type f

# Start Gunicorn with the correct WSGI path
exec gunicorn django_portfolio_app.portfolio_app.wsgi:application