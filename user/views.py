from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import RegistrationForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Отправка приветственного письма
            send_mail(
                'Добро пожаловать!',
                'Спасибо за регистрацию на нашем сайте.',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Замена на URL, куда необходимо перейти
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})