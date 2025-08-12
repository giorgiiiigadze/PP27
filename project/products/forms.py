from django import forms
from .models import Product

# model-based forma 
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'in_stock']



