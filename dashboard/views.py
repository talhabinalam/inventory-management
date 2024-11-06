from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)
