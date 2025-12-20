from tempfile import template
from .views import custom_logout
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import path, include
from user.apps import UserConfig
from user.views import UserCreateView

app_name = UserConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
]