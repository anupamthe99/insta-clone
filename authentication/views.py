from email import message
from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import LoginForm,SignUpForm
from django import forms
from django.contrib.auth.models import User
# Create your views here.
from django.contrib import messages
def user_login(request):
    wrong=False
    if request.method=="POST":
    
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("home")

        else:
            # Return an 'invalid login' error message.
            print("Invalid password")
            wrong=True
            context={
                "wrong":wrong,
                "form":LoginForm
            }
            return render(request,"authentication-file/login.html",context)
    context={
        "form":LoginForm
    }
    return render(request,"authentication-file/login.html",context)

def signup(request):
    # This are also some ways to do signup users
    
    # if request.method=="POST":
    # form = UserCreationForm(request.POST)
    # if form.is_valid():
    #     form.save()
    #     username = form.cleaned_data.get('username')
    #     raw_password = form.cleaned_data.get('password1')
    #     user = authenticate(username=username, password=raw_password)
    #     login(request, user)
    #     return redirect('profile_info')
    # else:
    #     form = UserCreationForm()
    # return render(request, 'authentication-file/signup.html', {'form': form})
    # sign_form=SignUpForm(request.POST or None)
    # if sign_form.is_valid():
    #     # sg=sign_form.save()
    #     sign_form.save()
    #     username=sign_form.cleaned_data.get('username')
    #     password=sign_form.cleaned_data.get('password1')
    #     # sg.set_password(password)
    #     # sg.save()
    #     user_auth=authenticate(username=username,password=password)
    #     login(request,user_auth)
    #     return redirect('profile-info')
    # else:
    #     sign_forms=SignUpForm(instance=request.POST)
    #     messages.error("Your account can not be created")
    # context={
    #     "form":sign_form
    # }
    # return render(request,"authentication-file/signup.html",context)
    
    
    form=SignUpForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        user_form=form.save(commit=False)
        # username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user_form.set_password(password)
        user_form.save()
        user_auth=authenticate(username=user_form.username,password=password)
        login(request,user_auth)
        return redirect("profile-info")
    return render(request,"authentication-file/signup.html",context)
def signout(request):
    logout(request)
    return redirect("login")