from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update-profile'),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
