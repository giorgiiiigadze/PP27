from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseNotAllowed
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

@login_required
def admin_update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        method = request.POST.get('_method', '').upper()
        if method == 'PUT':
            if not request.user.is_superuser:
                return HttpResponseForbidden('Only admin can change this product.')
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('product_detail', pk=product.pk)
        else:
            return HttpResponseNotAllowed(['PUT'])
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/admin_update_product.html', {
        'form': form,
        'product': product
    })
