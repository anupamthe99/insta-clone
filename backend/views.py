from multiprocessing import context
from django.shortcuts import render,redirect
from .models import post,like
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from authentication.signform import signup
from django.contrib.auth.forms import UserCreationForm
from .forms import user_profile
from .models import user_insta

# Create your views here.
def index(request):
    posts=post.objects.all()
    # user_profile=user_insta.objects.get(name=request.user)
    user_profile="hola"
    context={
        "posts":posts,
        "mero_naam":user_profile
    }
    return render(request,"index.html",context)

@login_required(login_url='login')
def upload(request):
    if request.method=="POST":
        pic=request.FILES.get("upload_image")
        caption=request.POST.get("caption")
        # users=request.user.get_username()
        
        # posts=post(caption=caption,like_count=0,pic=pic,user=User.get_username)
        posts=post.objects.create(caption=caption,like_count=0,pic=pic,userr=request.user)
        posts.save()
        return redirect("home")
    return render(request,"upload.html")

def profile(request,slug):
    posts=post.objects.filter(name=slug)    
    context={
        "posts":posts
    }
    return render(request,"profile.html",context)

def edit(request):
    mero_form=UserCreationForm(request.POST)
    edit_form=signup(instance=request.user)
    context={
        "edit_form":edit_form,
        "form":mero_form
    }
    return render(request,"edit.html",context)
    
def like_post(request):
    post_id=request.POST.get("post_id")
    username=request.user.username
    # likee=like.objects.filter(id=post_id)
    post_like=post.objects.filter(id=post_id,userr=username).first()

    if post_like==None:
        like_log=like.objects.create(user_id=post_id,username=username)
        like_log.save()
    else:
        like_log=like.objects.delete(id=post_id)
        like_log.save()
    return redirect("home")

def search_username(request):
    username=request.GET["search_username"]
    user_username=User.objects.filter(username__icontains=username)
    context={
        "users":user_username
    }
    return render(request,"search.html",context)

def search_profile(request):
    return render(request,"search_profile.html")

def profile_info(request):
    user=user_profile(request.POST or None,request.FILES or None)
    context={
        "form":user
    }
    if user.is_valid():
        user_info=user.instance
        user_info.username=request.user
        user_info.followers=0
        user_info.following=0
        user_info.post_num=0
        user_info.save()
        return redirect("profile")
    return render(request,"profile_info.html",context)
    

        
        
        
        