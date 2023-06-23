from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
@login_required(login_url='login/')
def admin_dashboard(request):
    print(userid_generator())
    return render(request, 'adminApp/home.html')


@login_required(login_url='login/')
def add_doctor(request):
    return render(request, 'adminApp/add_doctor.html')

def userid_generator():
    return random.randint(100000, 999999)