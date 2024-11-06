from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('staff/', staff, name='staff'),
    path('product/', product, name='product'),
    path('order/', order, name='order'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
