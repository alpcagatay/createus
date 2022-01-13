from django import forms
from django.core import validators
from django.db import models
import datetime
from django.db.models.fields import related
from django.db.models.fields.related import ManyToManyField
from django.forms import widgets
from django.forms.models import ModelForm
from django.contrib.auth.models import User


class MyClubUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    role = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to = "images/profile/")
    
    def __str__(self):
        return str(self.user)

class UserStory(models.Model):
    
    first= models.TextField(default="As")
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    second = models.TextField(default="I would like to")
    who = models.TextField()
    third = models.TextField(default="so that I can")
    desire = models.TextField()
    reason = models.TextField()
    

