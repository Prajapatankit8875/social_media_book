from django.urls import path
from . import views

urlpatterns = [
    path('create', views.Post_create, name='create'),
    path('feed', views.feed, name='feed'),  
    path('like', views.like_post, name='like'),
]