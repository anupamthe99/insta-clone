from ast import BinOp
from distutils.command.upload import upload
import email
from pickle import TRUE
from tkinter import CASCADE
from tkinter.tix import Tree
from tokenize import blank_re
from django.db import models
from requests import request

from authentication.views import user_login
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    caption=models.CharField(blank=True,max_length=100)
    like_count=models.IntegerField(default=0)
    pic=models.ImageField(upload_to="insta_pic")
    userr=models.ForeignKey(User,on_delete=models.CASCADE,default="")

    def __str__(self):
        return  f"caption:{self.caption}"

class like(models.Model):
    user_id=models.IntegerField()
    username=models.CharField(max_length=100,default="")
    
class user_insta(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    bio=models.CharField(max_length=70,blank=True)
    proflie_pic=models.ImageField(upload_to="profile_pic",blank=True)
    followers=models.IntegerField(default=0)
    following=models.IntegerField(default=0)
    post_num=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class commentPost(models.Model):
    sn=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_comment=models.ForeignKey(post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamps=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment
    
    

