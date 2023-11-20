from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile 


def home(request):
    return render(request, 'userlogin/home.html') 

@login_required
def user_info(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # If the user does not have a profile, create one
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('userinfo')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'userlogin/userinfo.html', {'user': request.user, 'form': form})

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

            # Check if UserProfile already exists for the user
            user_profile, created = UserProfile.objects.get_or_create(user=user)

            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)

            messages.success(request, 'Sign up successful. Please log in.')
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'userlogin/signup.html', {'form': form})


