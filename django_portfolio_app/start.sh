#!/bin/bash
# Set environment variable
export RENDER=true
# Start Gunicorn
cd /opt/render/project/src
gunicorn django_portfolio_app.portfolio_app.wsgi:application