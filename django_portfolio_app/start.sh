#!/bin/bash
cd /usr/local/Python/Projects/portfolio_app

export PYTHONPATH=$PYTHONPATH:/usr/local/Python/Projects/portfolio_app/django_portfolio_app

gunicorn portfolio_app.wsgi:application