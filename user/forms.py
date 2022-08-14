from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfileModel
from django import forms

#to add email field to sign_up form
class SignUpForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']


#to remove help documention under each field
    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        for fieldname in['username', 'email', 'password1', 'password2']:
                self.fields[fieldname].help_text=None

#to update the data in user model from profile page
class UserUpdateForm(forms.ModelForm):
        
    class Meta:
        model = User
        fields = ['username','email']
    #to remove help documention under each field
    def __init__(self,*args,**kwargs):
        super(UserUpdateForm,self).__init__(*args,**kwargs)
        for fieldname in['username', 'email']:
                self.fields[fieldname].help_text=None

#to update the profile image 
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = ProfileModel
        fields = ['image']
