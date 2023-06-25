from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        log = authenticate(username=username, password=password)
        if log is not None:
            login(request, log)
            if request.user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('patient_homepage')
        else:
            messages.error(request, 'Invalid Username or Password.')
    return render(request, 'main/login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get('password')
        if len(User.objects.filter(email=email)) == 0 and len(User.objects.filter(username=username)) == 0:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'User profile is created.')
        else:
            messages.error(request, 'User is already available.')
    return render(request, 'main/signup.html')


def contactus(request):
    return render(request, 'main/contactus.html')


@login_required(login_url='/login/')
def userLogout(request):
    '''Logout the active user and redirect to home page'''
    logout(request)
    return redirect('login')
