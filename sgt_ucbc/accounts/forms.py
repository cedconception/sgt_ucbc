from django import forms
from django.contrib.auth.forms import UserCreationForm, get_user_model
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

User = get_user_model()
class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email' ]
