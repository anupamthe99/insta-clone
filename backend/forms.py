from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import user_insta



class user_profile(ModelForm):
    class Meta:
        model=user_insta
        fields=["name","email","bio","proflie_pic"]

