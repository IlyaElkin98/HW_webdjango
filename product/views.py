from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from product.forms import ProductForm
from .models import Category, Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_form.html"
    success_url = reverse_lazy("product:products")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_form.html"
    success_url = reverse_lazy("product:products")
    permission_required = 'product.change_product'

    def has_permission(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm('product.can_delete_product')


class ProductListView(ListView):
    model = Product
    form_class = ProductForm
    template_name = "product/products.html"
    context_object_name = "products"

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_detail.html"
    context_object_name = "product"

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "product/product_confirm_delete.html"
    success_url = reverse_lazy("product:products")
    permission_required = 'product.delete_product'

    def has_permission(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm('product.can_delete_product')

    def delete(self, request, *args, **kwargs):
        if not self.has_permission():
            return HttpResponseForbidden('У вас нет прав на удаление продуктов')
        return super().delete(request, *args, **kwargs)

class ProductPublicationStatusView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm('product.can_unpublish_product'):
            return HttpResponseForbidden('У вас нет прав на снятия публикации продукта')

        product.publication_status = True
        product.save()
        return redirect('product:products')



# Представление для получения списка продуктов по категории
def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'product/products_by_category.html', {'category': category, 'products': products})

# Представление для получения списка всех категорий
def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'product/categories_list.html', {'categories': categories})


