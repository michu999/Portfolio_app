from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.accounts_profile, name='profile'),  # Example view
]