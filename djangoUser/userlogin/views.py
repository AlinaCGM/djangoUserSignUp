from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
                login(request, user)
                messages.success(request, 'Login successful. Welcome!')
                return redirect('userinfo')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()
    return render(request, 'userlogin/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)

            # Add success message
            messages.success(request, 'Sign up successful. Please log in.')

            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'userlogin/signup.html', {'form': form})



