from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from user.models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password1')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable help text for password fields
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']

