from email import message
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import post,like
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from authentication.signform import signup
from django.contrib.auth.forms import UserCreationForm
from .forms import user_profile
from .models import user_insta,commentPost
from django.contrib import messages
from backend.templatetags import extras
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@login_required(login_url='login')
def index(request):
    comment_pic=user_insta.objects.get(username=request.user)
    posts=post.objects.all()
    context={
        "posts":posts,
        "pic":comment_pic
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
@login_required(login_url='login')
def profile(request,pk):
    # slug=request.POST.get("")
    user=User.objects.get(username=pk)
    posts=post.objects.filter(userr=user)
    user_info=user_insta.objects.get(username=user)

        
    context={
        "posts":posts,
        "user_info":user_info
    }
    return render(request,"profile.html",context)
@login_required(login_url='login')
def edit(request,slug):
    
    # mero_form=UserCreationForm(request.POST)
    # edit_form=signup(instance=request.user)
    # context={
    #     "edit_form":edit_form,
    #     "form":mero_form
    # }
    # return render(request,"edit.html",context)
    user_info=user_insta.objects.get(id=slug)
    if request.method=="POST":
        form=user_profile(request.POST or None,request.FILES or None,instance=user_info)
        if form.is_valid():
            form.save(commit=False)
            form_edit=form.instance
            form_edit.username=request.user
            form_edit.followers=0
            form_edit.following=0
            form_edit.post_num=0
            form_edit.save()
            messages.success(request,"Your profile has been updated")
            return redirect("profile",user_info.username)
    else:
        form=user_profile(instance=user_info)
    context={
        "edit_form":form
    }
    return render(request,"edit.html",context)
@login_required(login_url='login')    
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
@login_required(login_url="login")
def search_username(request):
    query=request.GET["search_username"]
    # user=User.objects.filter(username__icontains=username)
    user_username=user_insta.objects.filter(username__username__icontains=query)
    context={
        "users":user_username
    }
    return render(request,"search.html",context)

def search_profile(request):
    return render(request,"search_profile.html")

@login_required(login_url='login')
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
        return redirect("home")
    return render(request,"profile_info.html",context)

@login_required(login_url="login")
def commentPostapi(request,slug):
    # posts=post.objects.get(post=slug)
    # comment=commentPost.objects.filter(post_comment=posts)
    if request.method=="POST":
        comment=request.POST.get("comment")
        post_sno=request.POST.get("sno")
        parentsno=request.POST.get("parentsno")
        post_comment=post.objects.get(id=post_sno)
        if parentsno=="":
            post_cmt=commentPost.objects.create(comment=comment,user=request.user,post_comment=post_comment)
            post_cmt.save()
            messages.success(request,"Comment has been posted")
        else:
            parent=commentPost.objects.get(sn=parentsno)
            post_cmt=commentPost.objects.create(comment=comment,user=request.user,post_comment=post_comment,parent=parent)
            post_cmt.save()
            messages.success(request,"Your reply has been posted")
    pt=post.objects.get(id=slug)       
    comment=commentPost.objects.filter(post_comment=pt,parent=None)
    replies=commentPost.objects.filter(post_comment=pt).exclude(parent=None)
    print("====================================================")
    print(replies)
    dict={}
    for r in replies:
        if r.sn not in replies:
            dict[r.sn]=r.comment
        else:
            dict[r.sn].append(r.comment)
    print(dict)
    # dict=list(dict)
    context={
        "comments":comment,
        "post":pt,
        "reply":dict
    }
    return render(request,"comment.html",context)       
    # context={
    #     "comments":comment
    # }
    # return render(request,"index.html",context)
# def comment(request,slug):
#     pt=post.objects.get(id=slug)       
#     comment=commentPost.objects.filter(post_comment=pt)
#     context={
#         "comments":comment,
#         "post":pt
#     }
#     return render(request,"comment.html",context)
        
        
        