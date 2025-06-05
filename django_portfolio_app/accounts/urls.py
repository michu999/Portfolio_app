from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<str:username>/', views.accounts_profile, name='profile'),
    path('profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),
]