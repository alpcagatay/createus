from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from django import forms
from django.db.models.base import Model
from django.forms import fields, ModelForm, widgets
from .models import UserStory, Category
from django.forms import inlineformset_factory


from django.contrib.auth import get_user_model
User = get_user_model()

class EditProfileForm(UserChangeForm):
    password = forms.CharField(label = "" ,widget = forms.TextInput())
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')


class CategoryForm(UserChangeForm):
    class Meta:
        model = Category
        fields =  ('name',)
        labels = {
            'name':'',
            
        }
        widgets= {
            'name': forms.TextInput(attrs={'placeholder':'e.g: Project 1 '})
          }
        


class SignUpForm(UserCreationForm):
    username = forms.CharField(label = "" ,max_length=150, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    email = forms.EmailField(label = "" ,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(help_text = "Enter Your First Name Here", label = "" ,max_length=100, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label = "" ,max_length=100,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    role = forms.CharField(label = "" ,max_length=1000,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'role'}))


    profile_picture = forms.ImageField()

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2','role','profile_picture')

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

        self.fields['profile_picture'].widget.attrs['class']= ''
        self.fields['profile_picture'].widget.attrs['placeholder']= ''
        self.fields['profile_picture'].label = ''
        self.fields['profile_picture'].help_text = ''

        self.fields['role'].widget.attrs['class']= 'form-control'
        self.fields['role'].widget.attrs['placeholder']= 'role'
        self.fields['role'].label = ''
        self.fields['role'].help_text = 'Please write your role.'



choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


class UserStoryForm(ModelForm):



    class Meta:
        model = UserStory
        fields =  ('category','who','desire','reason')
        labels = {
            'category':'',
            'who':'As',
            'desire':'I would like to',
            'reason':'so that I can '
        }
        widgets= {
            'category': forms.Select(choices = choice_list),
            'who': forms.TextInput(attrs={'placeholder':'e.g: User '}),
            'desire': forms.TextInput(attrs={'placeholder':'e.g: see the statuses'}),
            'reason': forms.TextInput(attrs={'placeholder':'e.g: I can list them'}),
              }
        
     
