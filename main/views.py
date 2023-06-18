from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def login(request):
    return render(request, 'main/login.html')


def signup(request):
    return render(request, 'main/signup.html')


def contactus(request):
    return render(request, 'main/contactus.html')
