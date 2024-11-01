from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

def product(request):
    products = Product.objects.all()
    return render(request, 'dashboard/product.html', {'products': products})

def order(request):
    orders = Order.objects.all()
    return render(request, 'dashboard/order.html', {'orders': orders})
