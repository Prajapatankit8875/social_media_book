from re import template 
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
]
