from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import DoctorInfo, DoctorSpecialization, Office, Qualification, DoctorAvailability


# Create your views here.
@login_required(login_url="/login/")
def doctor_dashboard(request):
    return render(request, "doctor/dashboard.html")


@login_required(login_url="/login/")
def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        userinfo = User.objects.get(username=request.user)
        if userinfo.check_password(old_password):
            userinfo.set_password(new_password)
            userinfo.save()
            return redirect("logout")
        else:
            messages.error(request, "Please enter correct password.")
    return render(request, "doctor/change_password.html")


@login_required(login_url="/login/")
def view_profile(request):
    doctorinfo = DoctorInfo.objects.get(userid=request.user)
    specialty = DoctorSpecialization.objects.get(userid=request.user)
    office = Office.objects.get(userid=request.user)
    qualification = Qualification.objects.get(userid=request.user)
    doctorAvailability = DoctorAvailability.objects.get(userid=request.user)
    return render(request, "doctor/view_profile.html",
                  {"doctorinfo": doctorinfo, "specialty": specialty, "office": office, "qualification": qualification,
                   "doctorAvailability": doctorAvailability})


@login_required(login_url="/login/")
def update_profile(request):
    doctorinfo = DoctorInfo.objects.get(userid=request.user)
    specialty = DoctorSpecialization.objects.get(userid=request.user)
    office = Office.objects.get(userid=request.user)
    qualification = Qualification.objects.get(userid=request.user)
    doctorAvailability = DoctorAvailability.objects.get(userid=request.user)
    if request.method == "POST":
        # qualification
        course_name = request.POST.get("course_name")
        institute_name = request.POST.get("institute_name")
        passing_year = request.POST.get("passing_year")
        # Availability
        day_of_week = request.POST.get("day_of_week")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        # Doctor Info
        practicing_year = request.POST.get("practicing_year")
        professional_statement = request.POST.get("professional_statement")
        # office
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        zipcode = request.POST.get("zipcode")
        time_slot_per_patient_time = request.POST.get("time_slot_per_patient_time")
        first_consultation_fee = request.POST.get("first_consultation_fee")
        followup_consultation_fee = request.POST.get("followup_consultation_fee")

        doctorinfo.professional_statement = professional_statement
        doctorinfo.practicing_year = practicing_year

        qualification.name = course_name
        qualification.institute_name = institute_name
        qualification.passing_year = passing_year

        doctorAvailability.day_of_week = day_of_week
        doctorAvailability.start_time = start_time
        doctorAvailability.end_time = end_time

        office.address1 = address1
        office.address2 = address2
        office.city = city
        office.state = state
        office.country = country
        office.zipcode = zipcode
        office.time_slot_per_patient_time = time_slot_per_patient_time
        office.first_consultation_fee = first_consultation_fee
        office.followup_consultation_fee = followup_consultation_fee
        
        doctorinfo.save()
        doctorAvailability.save()
        qualification.save()
        office.save()
        return redirect("view_profile")

    return render(request, "doctor/edit_profile.html",
                  {"doctorinfo": doctorinfo, "specialty": specialty, "office": office, "qualification": qualification,
                   "doctorAvailability": doctorAvailability})
