from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *

@login_required
def index(request):
    return render(request, 'dashboard/index.html')


@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')


@login_required
def product(request):
    products = Product.objects.all()
    return render(request, 'dashboard/product.html', {'products': products})


@login_required
def order(request):
    orders = Order.objects.all()
    return render(request, 'dashboard/order.html', {'orders': orders})


