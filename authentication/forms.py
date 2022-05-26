from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import signup
from django.contrib.auth.forms import UserCreationForm


class LoginForm(ModelForm):
    class Meta:
        model=User
        fields=["username","password"]

class SignUpForm(ModelForm):
    class Meta:
        model=signup
        fields=["username","email","password1","password2"]        
