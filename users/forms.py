from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  # default form in django
from .models import Profile

class UserRegisterForm(UserCreationForm):
    # adding extra field
    
    email = forms.EmailField()
    
    class Meta():
        model = User
        fields = ['username','email','password1','password2']
        
# Update profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta():
        model = User
        fields = ['username','email']
        
# for profile pic

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        