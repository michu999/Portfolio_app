from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

try:
    import accounts
except ImportError:
    AUTH_USER_MODEL = 'auth.User'
    INSTALLED_APPS = [app for app in INSTALLED_APPS if app != 'accounts'
                      and not app.startswith('allauth')]