from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, forms
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
