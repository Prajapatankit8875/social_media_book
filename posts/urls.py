from django.urls import path
from . import views

urlpatterns = [
    path('create', views.Post_create, name='create'),
]