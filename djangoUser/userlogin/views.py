from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'userlogin/home.html')

@login_required
def user_info(request):
    return render(request, 'userlogin/userinfo.html', {'user': request.user})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                print("User is not None")
                login(request, user)
                print("Redirecting to userinfo")  
                return redirect('userinfo') 
            else:
                print("User is None")
    else:
        form = LoginForm()
    return render(request, 'userlogin/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = SignupForm()

    return render(request, 'userlogin/signup.html', {'form': form})


