from django.contrib.auth import logout, login
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages

from user.forms import UserRegisterForm
from user.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:login')


def custom_logout(request):
    logout(request)

    return redirect('product:products')