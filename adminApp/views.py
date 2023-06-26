from random import shuffle, choices
from string import digits, ascii_lowercase, ascii_uppercase

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render

from doctor.models import DoctorInfo, DoctorSpecialization
from .models import Specialty


# Create your views here.
@login_required(login_url='/login/')
def admin_dashboard(request):
    doctor_list = DoctorInfo.objects.all()
    return render(request, 'adminApp/home.html', {"main": doctor_list})


@login_required(login_url='/login/')
def add_doctor(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        specialty = request.POST.get("specialty")
        username = email[:email.rindex("@")]
        try:
            User.objects.create_user(username=username, email=email, password="7upNim@karn")
            doctor = DoctorInfo.objects.create(userid=User.objects.get(username=username), firstname=firstname,
                                               lastname=lastname,
                                               phone=phone, gender=gender)
            doctor.save()
            specialty = DoctorSpecialization(userid=User.objects.get(username=username),
                                             specialization_id=Specialty.objects.get(name=specialty))
            specialty.save()
            messages.success(request, "Successfully is added")
        except IntegrityError:
            messages.error(request, "The user is already added")
    specialty_list = Specialty.objects.all()
    return render(request, 'adminApp/add_doctor.html', {"main": specialty_list})


@login_required(login_url='/login/')
def view_specialty(request):
    specialty_list = Specialty.objects.all()
    return render(request, "adminApp/specialty_list.html", {"main": specialty_list})


@login_required(login_url='/login/')
def add_specialty(request):
    if request.method == "POST":
        specialty = request.POST.get("specialty")
        try:
            Specialty(name=specialty).save()
            messages.success(request, "Successfully added")
        except IntegrityError:
            messages.error(request, "It is already added")
    return render(request, "adminApp/add_specialty.html")


def _password_generator():
    lower_letter = choices([i for i in ascii_lowercase], k=4)
    digit = choices([i for i in digits], k=3)
    upper_letter = choices([i for i in ascii_uppercase], k=1)
    new_password = lower_letter + digit + upper_letter
    shuffle(new_password)
    return new_password
