from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.forum, name='forum'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/comment/<int:parent_id>/', views.add_comment, name='add_comment'),
    path('add_post/', views.add_post, name='add_post'),
    path('reaction/toggle/', views.toggle_reaction, name='toggle_reaction'),
    path('post/<int:post_id>/comment/<int:parent_id>/reply/', views.add_comment, name='add_reply'),
]