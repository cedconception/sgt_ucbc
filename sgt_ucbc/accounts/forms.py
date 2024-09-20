from django import forms
from django.contrib.auth.forms import UserCreationForm, get_user_model
from .models import User


#User = get_user_model()

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email' ]

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from .models import FacultyProfile, StudentProfile

class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model = FacultyProfile
        fields = ['department', 'faculty_position', 'faculty_contact_email']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['student_id', 'department', 'supervisor']

