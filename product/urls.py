from django.urls import path
from django.conf import settings
from django.views.decorators.cache import cache_page

from .views import ProductCreateView, ProductListView, ProductDeleteView, ProductUpdateView, ProductDetailView, \
    ProductPublicationStatusView
from product.apps import ProductConfig


app_name = ProductConfig.name


urlpatterns = [
    path("products/", ProductListView.as_view(), name="products"),
    path("products/product_form/", ProductCreateView.as_view(), name="create_product"),
    path("products/delete_product/<int:pk>/", ProductDeleteView.as_view(), name="delete_product"),
    path("products/detail_product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="detail_product"),
    path("products/detail_product/<int:pk>/update/", ProductUpdateView.as_view(), name="update_product"),
    path("products/can_unpublish_product/<int:pk>/", ProductPublicationStatusView.as_view(), name="can_unpublish_product"),

]