from email.policy import default
from unicodedata import category
from django import forms
from django.core import validators
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import related
from django.db.models.fields.related import ManyToManyField
from django.forms import widgets
from django.forms.models import ModelForm
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.urls import reverse



# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if email:
            email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name="Username",
        max_length=150,
        blank=False,
        null=False,
        unique=True
    )
    email = models.EmailField(
        verbose_name="Email address",
        max_length=96,
        blank=True,
        null=True
    )
    first_name = models.CharField(
        verbose_name="First name",
        max_length=30,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        verbose_name="Last name",
        max_length=30,
        blank=True,
        null=True
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name="Date joined"
    )
    is_superuser = models.BooleanField(
        verbose_name="Super user",
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name="Staff",
        default=False
    )
    is_active = models.BooleanField(
        verbose_name="Active",
        default=True
    )
    profile_picture = models.ImageField(
        verbose_name="Profile picture",
        null=True, 
        blank=True, 
        upload_to = "images/profile/"
    )
    role = models.TextField(
        verbose_name="role",
        blank=True,
        null=True
    )
    numberofus = models.PositiveBigIntegerField(
        verbose_name="numberofus",
        default=0, 
        validators = [MaxValueValidator(1000),MinValueValidator(0)],
    )
    rookie = models.TextField(
        verbose_name="rookie",
        blank=True,
        null=True
    )
   
    
    


    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return " ".join([self.first_name, self.last_name])


class Category(models.Model):
    name = models.CharField(max_length=255)

    

class UserStory(models.Model):
    
    
    category = models.CharField(max_length=255, default="Category1")
    first= models.TextField(default="As")
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    second = models.TextField(default="I would like to")
    who = models.TextField()
    third = models.TextField(default="so that I can")
    desire = models.TextField()
    reason = models.TextField()
    likes = models.ManyToManyField(User, blank = True, related_name = 'like')
    dislikes = models.ManyToManyField(User, blank = True, related_name = 'dislike')
    numberoflikes = models.PositiveBigIntegerField(default = 0)
    numberofdislikes = models.PositiveIntegerField(default = 0)

