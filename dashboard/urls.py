from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', index, name='dashboard'),
    path('staff/', staff, name='staff'),
    path('product/', product, name='product'),
    path('order/', order, name='order'),
]
