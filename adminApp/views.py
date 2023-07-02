from random import shuffle, choices
from string import digits, ascii_lowercase, ascii_uppercase

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from doctor.models import DoctorInfo, DoctorSpecialization, Office, Qualification, DoctorAvailability
from .models import Specialty


# Create your views here.
@login_required(login_url='/login/')
def admin_dashboard(request):
    return render(request, 'adminApp/dashboard.html')


@login_required(login_url='/login/')
def doctor_list(request):
    doctors = DoctorInfo.objects.all()
    return render(request, 'adminApp/doctor_list.html', {"main": doctors})


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
            User.objects.create_user(username=username, email=email, password=password_generator())
            doctor = DoctorInfo(userid=User.objects.get(username=username), firstname=firstname,
                                lastname=lastname,
                                phone=phone, gender=gender)
            doctor.save()
            specialty = DoctorSpecialization(userid=User.objects.get(username=username),
                                             specialization_id=Specialty.objects.get(name=specialty))
            specialty.save()
            office = Office(userid=User.objects.get(username=username))
            office.save()
            qualification = Qualification(userid=User.objects.get(username=username))
            qualification.save()
            doctorAvailability = DoctorAvailability(userid=User.objects.get(username=username))
            doctorAvailability.save()
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


@login_required(login_url='/login/')
def password_sent(request, userid):
    userinfo = User.objects.get_by_natural_key(userid)
    password = password_generator()
    userinfo.set_password(password)
    userinfo.save()
    subject = "Doctor profile verification"
    message = f"""
    Hello Doctor, \n
    \tYour profile is successfully created. Your userid {userid} and password {password}.\nPlease, never share your userid and password to any one. Change your password on first login.
    \nI hope we will provide you a better experience.
    Thank You, 
    Admin
    """
    _emailSend(subject, message, userinfo.email)
    doc = DoctorInfo.objects.get(userid=userinfo)
    doc.is_password_sent = True
    doc.save()
    return redirect("doctor_list")


@login_required(login_url='/login/')
def import_specialty_data(request):
    return render(request, "adminApp/import_specialty.html")


@login_required(login_url='/login/')
def import_doctor_data(request):
    return render(request, "adminApp/import_doctor.html")


def password_generator():
    lower_letter = choices([i for i in ascii_lowercase], k=4)
    digit = choices([i for i in digits], k=3)
    upper_letter = choices([i for i in ascii_uppercase], k=1)
    new_password = lower_letter + digit + upper_letter
    shuffle(new_password)
    return "".join(new_password)


def _emailSend(*args):
    email = EmailMessage(subject=args[0], body=args[1], to=[args[2]])
    email.send()
    return HttpResponse(status=204)
