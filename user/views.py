from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.forms import UserRegisterForm
from user.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "product/product_form.html"
    success_url = reverse_lazy("user:login")

