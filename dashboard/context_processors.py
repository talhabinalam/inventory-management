from django.contrib.auth.models import User
from .models import *

def global_counters(request):
    user = request.user
    if user.is_authenticated:
        staff_count = User.objects.count()
        product_count = Product.objects.count()
        order_count = Order.objects.count() if user.is_superuser else Order.objects.filter(staff=user).count()
    else:
        staff_count = 0
        product_count = 0
        order_count = 0

    return {
        'staff_count': staff_count,
        'product_count': product_count,
        'order_count': order_count
    }
