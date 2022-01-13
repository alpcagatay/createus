from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from django import forms
from django.db.models.base import Model
from django.forms import fields, ModelForm, widgets
from .models import MyClubUser, UserStory



class EditProfileForm(UserChangeForm):
    password = forms.CharField(label = "" ,widget = forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password',)



class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = "" ,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(help_text = "Enter Your First Name Here", label = "" ,max_length=100, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label = "" ,max_length=100,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['username'].widget.attrs['placeholder']= 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'




        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['placeholder']= 'Password'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['placeholder']= 'Confirm Password'
        self.fields['password2'].label = ''

class UserStoryForm(ModelForm):
    class Meta:
        model = UserStory
        fields =  ('who','desire','reason')
        labels = {
            'who':'As',
            'desire':'I would like to',
            'reason':'so that I can '
        }
        widgets= {
            'who': forms.TextInput(attrs={'placeholder':'Service Name'}),
            'desire': forms.TextInput(attrs={'placeholder':'Service Name'}),
            'reason': forms.TextInput(attrs={'placeholder':'Service Name'}),
              }
