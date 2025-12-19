from tempfile import template

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from user.apps import UserConfig

app_name = UserConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', LogoutView.as_view(template_name='logout.html'))
]