#!/bin/bash
gunicorn portfolio_app.wsgi:application