#!/bin/bash
# Move into the project directory
cd /opt/render/project/src
# Install dependencies
pip install -r requirements.txt
# Run migrations
python manage.py migrate