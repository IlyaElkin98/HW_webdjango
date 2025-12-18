from django.urls import reverse_lazy,reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from product.models import Product
from product.forms import ProductForm


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_form.html"
    success_url = reverse_lazy("product:products")

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_form.html"
    success_url = reverse_lazy("product:products")

class ProductListView(ListView):
    model = Product
    form_class = ProductForm
    template_name = "product/products.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_detail.html"
    context_object_name = "product"

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product/product_confirm_delete.html"
    success_url = reverse_lazy("product:products")

