from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('contact/', views.contact_view, name='contact'),
]
