import os
from django.core.wsgi import get_wsgi_application

# Use production settings on Vercel
if 'VERCEL_REGION' in os.environ:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_app.production_settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_app.settings')

application = get_wsgi_application()
app = application  # For Vercel