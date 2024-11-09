from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from user.forms import ProfileUpdateForm
from .models import *
from .forms import *

@login_required
def index(request):
    return render(request, 'dashboard/index.html')


@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')


@login_required
def product(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product has been added successfully!")
            return redirect('product')
    else:
        form = ProductForm()
    context = {
        'products': products,
        'form' : form
    }
    return render(request, 'dashboard/product.html', context)


def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product has been updated!")
            return redirect('product')
    else:
        form = ProductUpdateForm(instance=product)
    context = {
        'product': product,
        'form': form
    }
    return render(request, 'dashboard/product-update.html', context)


def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect('product')


@login_required
def order(request):
    orders = Order.objects.all()
    return render(request, 'dashboard/order.html', {'orders': orders})


