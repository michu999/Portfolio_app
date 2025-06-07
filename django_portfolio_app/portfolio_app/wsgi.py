import os
from django.core.wsgi import get_wsgi_application

if os.environ.get('RENDER', '') == 'true':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_portfolio_app.portfolio_app.settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_portfolio_app.portfolio_app.settings')

application = get_wsgi_application()
app = application