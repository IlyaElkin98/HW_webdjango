from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(upload_to="user/avatars/" ,width_field=150, height_field=150, verbose_name="Аватар", help_text="Загрузите аватар", null=True, blank=True)
    phone_number = models.CharField(blank=True, help_text="Укажите номер телефона", null=True)
    country = models.CharField(max_length=50, verbose_name="Страна", help_text="Укажите страну", blank=True, null=True)
    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

        def __str__(self):
            return self.email
