
from inspect import ArgSpec
from itertools import count
from pdb import post_mortem
from django.http import request, HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import CategoryForm, EditProfileForm, SignUpForm, UserStoryForm
from urllib.parse import urlencode
from urllib.parse import urlparse, parse_qsl
from .models import Category, UserStory
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.forms import modelformset_factory
import csv
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Min, Sum




def add_category(request):
    submitted = False
    if request.method == "POST":
        form2 = CategoryForm(request.POST)
        if form2.is_valid():
            category = form2.save(commit=False)
            category.save()
            return HttpResponseRedirect('/add_category?submitted=True')
    else: 
        form2 = CategoryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_category.html', {'form2':form2, 'submitted':submitted})



User = get_user_model()

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
        form = SignUpForm(request.POST, request.FILES)
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

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
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
        form = UserStoryForm(request.POST)
        if form.is_valid():
            user = request.user
            userstory = form.save(commit=False)
            userstory.owner = user
            userstory.save()
            user.numberofus = user.numberofus + 1
            user.save() 
             
            return HttpResponseRedirect('/add_user_story?submitted=True')
    else: 
        form = UserStoryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_user_story.html', {'form':form, 'submitted':submitted})


def my_user_stories(request):
    if request.user.is_authenticated:
        me = request.user.id
        userstory = UserStory.objects.filter(owner = me)
        return render(request, 'my_user_stories.html', {'me':me, 'userstory':userstory})
    else:
        messages.success(request, ("You are not logged in"))
        return redirect('login')

def userstory_csv(request):
    
    me = request.user.id
    response = HttpResponse(content_type ='text/csv' )
    response['Content-Disposition'] = 'attachment; filename = userstory.csv'

    # Create a writer
    writer = csv.writer(response)

    #Designate the model
    userstory = UserStory.objects.all()

    # Add column headings
    writer.writerow(['Project','First','Who','Second','Desire','Third','Reason'])

   
        #Loop through and output.
    for userstory in userstory:
        writer.writerow([(userstory.category),(userstory.first),(userstory.who),(userstory.second),(userstory.desire),(userstory.third),(userstory.reason)])


    return response

@login_required
def update_userstory(request,userstory_id):
    userstory = UserStory.objects.get(pk = userstory_id)
    form = UserStoryForm(request.POST or None,request.FILES,instance = userstory)
    if form.is_valid():
        form.save()
        return redirect('list_events')
    return render(request, 'update_event.html', {'userstory':userstory, 'form': form})


@login_required
def list_userstories(request):
    userstories = UserStory.objects.all()
    return render(request, 'list_userstories.html', {'userstories': userstories })

@login_required
def delete_userstory(request, userstory_id):
    user = request.user
    userstory = UserStory.objects.get(pk = userstory_id)
    userstory.delete()
    user.numberofus = user.numberofus - 1
    user.save()
    messages.success(request,("Userstory deleted!"))
    return HttpResponseRedirect('/list_userstories')

@login_required
def update_userstory(request,userstory_id):
    userstory = UserStory.objects.get(pk = userstory_id)
    form = UserStoryForm(request.POST or None,request.FILES, instance = userstory)
    if form.is_valid():
        form.save()
        return redirect('list_userstories')
    return render(request, 'update_userstory.html', {'userstory':userstory, 'form': form})

def badges(request):
    return render(request, 'badges.html')

def leaderboard(request):
    user_list = User.objects.all().order_by('-numberofus')

    return render(request, 'leaderboard.html',{'user_list':user_list})
    # if request.user.is_authenticated:
    #     users = User.objects.all
    #     userslist = []
    #     for user in users:
    #         userslist.append(user) 
    #         user.numberofus = (UserStory.objects.filter(owner = user)).count()
    #         user.save()
    #     return render(request, 'leaderboard.html')
   
    # else:
    #     messages.success(request, ("You are not logged in"))
    #     return redirect('login')
