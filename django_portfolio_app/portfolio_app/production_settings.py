from .settings import *
import importlib
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration using environment variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'portfolio_db_vpeo'),
        'USER': os.environ.get('DB_USER', 'portfolio_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'dpg-d10rst49c44c73e17vh0-a.frankfurt-postgres.render.com'),
        'PORT': os.environ.get('DB_PORT', '5432'),
        'OPTIONS': {
            'sslmode': 'require',
        }
    }
}

# Path configurations to find your apps
sys.path.insert(0, os.path.join(BASE_DIR, '..'))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Add whitenoise for static files
if 'whitenoise.middleware.WhiteNoiseMiddleware' not in MIDDLEWARE:
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security settings for production
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '.vercel.app,localhost,127.0.0.1').split(',')

# Debug info only if DEBUG is True
if DEBUG:
    print("BASE_DIR:", BASE_DIR)
    print("sys.path:", sys.path)
    print("INSTALLED_APPS:", INSTALLED_APPS)

    # Try to import each app to identify which ones are problematic
    for app in INSTALLED_APPS:
        try:
            importlib.import_module(app)
            print(f"Successfully imported {app}")
        except ImportError as e:
            print(f"Failed to import {app}: {e}")