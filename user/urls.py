from tempfile import template

from django.contrib.auth.views import PasswordResetView
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
