from .settings import *
import importlib
import sys

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

sys.path.insert(0, os.path.join(BASE_DIR, '..'))


try:
    import accounts
except ImportError:
    AUTH_USER_MODEL = 'auth.User'
    INSTALLED_APPS = [app for app in INSTALLED_APPS if app != 'accounts'
                      and not app.startswith('allauth')]