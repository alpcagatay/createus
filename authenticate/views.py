from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import EditProfileForm, SignUpForm, UserStoryForm
from urllib.parse import urlencode
from urllib.parse import urlparse, parse_qsl
from .models import MyClubUser
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,'home.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('You have been logged in.'))
            return redirect('home')
        else:
            messages.success(request,('Ooops! Something went wrong. Please Try Again.'))
            return redirect('login')  
    else:
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,('You have been logged out!'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username = username, password=password)
            login(request,user)
            messages.success(request,('You have registered'))
            return redirect('home')

    else:
        form = SignUpForm()
    
    context = {'form':form}
    return render(request, 'register.html',context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
           
            messages.success(request,('You have edited your profile'))
            return redirect('home')

    else:
        form = EditProfileForm(instance=request.user)
    
    context = {'form':form}
    return render(request, 'edit_profile.html',context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(date=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,('You have edited your password'))
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)
    
    context = {'form':form}
    return render(request, 'change_password.html',context)

def user_profile(request):
    return render(request, 'user_profile.html')


def add_user_story(request):
    submitted = False
    if request.method == "POST":
        form = UserStoryForm(request.POST, request.FILES)
        if form.is_valid():
            userstory = form.save(commit=False)
            userstory.owner = request.user
            userstory.save()
            return HttpResponseRedirect('/add_user_story?submitted=True')
    else: 
        form = UserStoryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_user_story.html', {'form':form, 'submitted':submitted})


