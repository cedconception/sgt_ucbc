from urllib import request
from django.shortcuts import redirect, render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Group
from .forms import FacultyProfileForm, StudentProfileForm


def not_authenticated(user):
    return not user.is_authenticated

def is_Faculty(user):
    return user.is_authenticated and user.groups.filter(name='Faculté').exists()



@user_passes_test(not_authenticated)
def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        student_group = Group.objects.get(name='Étudiant')
        user.groups.add(student_group)
        return redirect(reverse("login"))
    else:
        form = UserCreationForm()
    return render(request, 'registration/create_account.html', { 'form': form })

def user_profile(request):
    return render(request, 'registration/profile.html')

@login_required
def change_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
        return redirect('accounts:profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'registration/change_profile.html', { 'form': form })
    

@login_required
def profile_view(request):
    if request.method == 'POST':
        if request.user.facultyprofile:
            form = FacultyProfileForm(request.POST, instance=request.user.facultyprofile)
        else:
            form = StudentProfileForm(request.POST, instance=request.user.studentprofile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = FacultyProfileForm(instance=request.user.facultyprofile) if request.user.facultyprofile else StudentProfileForm(instance=request.user.studentprofile)
    return render(request, 'profileView.html', {'form': form})