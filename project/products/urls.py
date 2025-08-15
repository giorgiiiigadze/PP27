from django.urls import path
# from . import views
from .views import ProductDetailView, ProductListView, AdminUpdateProductView, AddProductView # *

urlpatterns = [
    path('products/', ProductListView.as_view(), name = 'product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name = 'product_detail'),
    path('add/', AddProductView.as_view(), name = 'add_product'),
    path('products/<int:pk>/admin-update/', AdminUpdateProductView.as_view(), name = 'admin_update_product'),
]


