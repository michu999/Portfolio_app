from .settings import *
import importlib
import sys
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# More aggressively adjust Python path to find your apps
sys.path.insert(0, os.path.join(BASE_DIR, '..'))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Debug info to log paths and installed apps
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

try:
    import accounts
except ImportError:
    AUTH_USER_MODEL = 'auth.User'
    INSTALLED_APPS = [app for app in INSTALLED_APPS if app != 'accounts'
                      and not app.startswith('allauth')]