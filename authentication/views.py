from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import LoginForm,SignUpForm

# Create your views here.
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
    sign_form=SignUpForm(request.POST or None)
    context={
        "form":sign_form
    }
    return render(request,"authentication-file/signup.html",context)
def signout(request):
    logout(request)
    return redirect("login")