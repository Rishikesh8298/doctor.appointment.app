import datetime as dt

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from module.dates import get_date_list
from module.pagination import create_pagination
from patient.models import PatientInfo
from .models import DoctorInfo, DoctorSpecialization, Office, Qualification, DoctorAvailability, Appointment, \
    Unavailability


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
    doctors = {
        "firstname": doctorinfo.firstname,
        "lastname": doctorinfo.lastname,
        "phone": doctorinfo.phone,
        "specialty": specialty.specialization_id.name,
        "professional_statement": doctorinfo.professional_statement,
        "practicing_year": str(doctorinfo.practicing_year),
        "course_name": qualification.name,
        "institute_name": qualification.institute_name,
        "passing_year": str(qualification.passing_year),
        "day_of_week": doctorAvailability.day_of_week,
        "start_time": str(doctorAvailability.start_time),
        "end_time": str(doctorAvailability.end_time),
        "address1": office.address1,
        "address2": office.address2,
        "city": office.city,
        "state": office.state,
        "country": office.country,
        "zipcode": office.zipcode,
        "time_slot_per_patient_time": office.time_slot_per_patient_time,
        "first_consultation_fee": office.first_consultation_fee,
        "followup_consultation_fee": office.followup_consultation_fee,
    }
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
        time_slot_per_patient_time = request.POST.get(
            "time_slot_per_patient_time")
        first_consultation_fee = request.POST.get("first_consultation_fee")
        followup_consultation_fee = request.POST.get(
            "followup_consultation_fee")

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
    return render(request, "doctor/edit_profile.html", {"doctors": doctors, })


@login_required(login_url='/login/')
def view_appointments(request):
    appointmentList = Appointment.objects.filter(doctor_id=DoctorInfo.objects.get(userid=request.user))
    pastAppointments = [i for i in appointmentList if i.appointment_date < dt.date.today() and i.status != "Cancel"]

    page = request.GET.get('page')
    main = create_pagination(main=pastAppointments, no=30, page=page)
    return render(request, "doctor/view_appointment.html", {"main": main})


@login_required(login_url='/login/')
def today_appointments(request):
    appointments = Appointment.objects.filter(doctor_id=DoctorInfo.objects.get(userid=request.user))
    appointmentList = [i for i in appointments if i.appointment_date == dt.date.today() and i.status == "Not-Visit"]
    return render(request, "doctor/today_appointment.html", {"appointmentList": appointmentList})


@login_required(login_url='/login/')
def upcoming_appointments(request):
    appointmentList = Appointment.objects.filter(doctor_id=DoctorInfo.objects.get(userid=request.user))
    scheduled = [i for i in appointmentList if i.appointment_date > dt.date.today() and i.status != "Cancel"]
    return render(request, "doctor/upcoming_appointments.html", {"main": scheduled})


@login_required(login_url='/login/')
def change_status(request, id):
    main = Appointment.objects.get(id=id)
    if request.method == "POST":
        status = request.POST.get("status")
        main.status = status
        main.save()
        return redirect("today_appointments")
    return render(request, "doctor/change_status.html", {"main": main})


@login_required(login_url='/login/')
def unavailability(request):
    doctor = DoctorAvailability.objects.get(userid=User.objects.get_by_natural_key(username=request.user))
    date_list = get_date_list(doctor.day_of_week)
    for i in Unavailability.objects.filter(
            doctor_id=DoctorInfo.objects.get(userid=User.objects.get_by_natural_key(username=request.user))):
        if str(i.date_of_unavailability) in date_list:
            date_list.remove(str(i.date_of_unavailability))
    if request.method == "POST":
        date_of_unavailability = request.POST.get("date")
        reason_of_unavailability = request.POST.get("reason")
        reason = Unavailability(
            doctor_id=DoctorInfo.objects.get(userid=User.objects.get_by_natural_key(username=request.user)),
            date_of_unavailability=date_of_unavailability,
            reason_of_unavailability=reason_of_unavailability)
        reason.save()
    return render(request, "doctor/reason_of_unavailability.html", {"date_list": date_list})


@login_required(login_url='/login/')
def view_patient_profile(request, patient_id):
    patient = PatientInfo.objects.get(userid=User.objects.get_by_natural_key(username=patient_id))
    return render(request, "doctor/view_patient_profile.html", {"patient": patient})


@login_required(login_url='/login/')
def unavailability_list(request):
    main = Unavailability.objects.filter(
        doctor_id=DoctorInfo.objects.get(userid=User.objects.get_by_natural_key(username=request.user))).order_by('-pk')
    return render(request, "doctor/list_of_unavailability.html", {"main": main})


@login_required(login_url='/login/')
def view_reason(request, id):
    main = Unavailability.objects.get(id=id)
    return render(request, "doctor/view_reason.html", {"main": main})


@login_required(login_url='/login/')
def search_appointments_by_date(request):
    if request.method == "POST":
        date = request.POST.get("date")
        appointmentList = Appointment.objects.filter(doctor_id=DoctorInfo.objects.get(userid=request.user),
                                                     appointment_date=date).exclude(status="Cancel")
        page = request.GET.get('page')
        main = create_pagination(main=appointmentList, no=30, page=page)
        return render(request, "doctor/search_appointments_by_date.html", {"main": main, "date": date})
    return redirect("view_appointments")
