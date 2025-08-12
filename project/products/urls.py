from django.urls import path
from . import views
# from .views import product_list
urlpatterns = [
    path('products/', views.product_list, name = 'product_list'),
    path('products/<int:pk>/', views.product_detail, name = 'product_detail'),
    path('add/', views.add_product, name = 'add_product'),
    path('products/<int:pk>/admin-update/', views.admin_update_product, name = 'admin_update_product'),
]


