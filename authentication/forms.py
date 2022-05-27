import imp
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import signup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


user=get_user_model()

class LoginForm(ModelForm):
    class Meta:
        model=User
        fields=["username","password"]

class SignUpForm(ModelForm):
    # address=forms.CharField(max_length=100)
    class Meta:
        model=user
        fields=["username","email","password"]        
