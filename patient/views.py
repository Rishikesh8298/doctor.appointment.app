import datetime as dt
import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from adminApp.models import Specialty
from doctor.models import DoctorInfo, DoctorSpecialization, DoctorAvailability, Office, Appointment
from module.dates import get_date_list
from module.pagination import create_pagination
from .models import PatientInfo, User


@login_required(login_url='/login/')
def patient_homepage(request):
    doctorInfo = DoctorInfo.objects.all()
    cities = set([i.city for i in Office.objects.all() if i.city is not None])
    cities = sorted(list(cities))
    doctors = []
    for i in doctorInfo:
        try:
            office = Office.objects.get(userid=i.userid)
            doctorAvailability = DoctorAvailability.objects.get(userid=i.userid)
            doctorSpecialization = DoctorSpecialization.objects.get(userid=i.userid)
        except:
            pass
        else:
            if office.address1 is not None and office.city is not None and office.state is not None and office.zipcode is not None:
                data = {'userid': i.userid,
                        'firstname': i.firstname,
                        'lastname': i.lastname,
                        'gender': i.gender,
                        'phone': i.phone,
                        'address1': office.address1,
                        'address2': office.address2,
                        'city': office.city,
                        'state': office.state,
                        'country': office.country,
                        'zipcode': office.zipcode,
                        'first_consultation_fee': office.first_consultation_fee,
                        'day_of_week': doctorAvailability.day_of_week,
                        'specialty': doctorSpecialization.specialization_id
                        }
                doctors.append(data)
    page = request.GET.get('page')
    main = create_pagination(main=doctors, no=30, page=page)
    appointments = [i for i in
                    Appointment.objects.filter(patient_id=PatientInfo.objects.get(
                        userid=User.objects.get_by_natural_key(username=request.user))) if
                    i.appointment_date >= dt.date.today()]
    return render(request, 'patient/home.html',
                  {"doctors": main, "cities": cities, "specialty": Specialty.objects.all(),
                   "appointments": appointments})


@login_required(login_url='/login/')
def take_appointment(request, doctor_id):
    doctor_info = DoctorInfo.objects.get(userid=User.objects.get_by_natural_key(username=doctor_id))
    availability = DoctorAvailability.objects.get(userid=User.objects.get_by_natural_key(username=doctor_id))
    office = Office.objects.get(userid=User.objects.get_by_natural_key(username=doctor_id))
    doctor = {
        "firstname": doctor_info.firstname,
        "lastname": doctor_info.lastname,
        "day_of_week": availability.day_of_week,
    }
    date_list = get_date_list(doctor["day_of_week"])
    if request.method == "POST":
        patient_ID = PatientInfo.objects.get(userid=request.user)
        appointment_date = request.POST.get("appointment_date")
        appointment_lists = Appointment.objects.filter(appointment_date=appointment_date, doctor_id=doctor_info.pk)
        probable_start_time = availability.start_time
        if len(appointment_lists) == 0:
            if str(office.time_slot_per_patient_time).endswith("min"):
                actual_end_time = dt.datetime.combine(dt.datetime.strptime(appointment_date, "%Y-%m-%d"),
                                                      probable_start_time) + dt.timedelta(
                    minutes=int(str(office.time_slot_per_patient_time)[:2])) + dt.timedelta(minutes=10)
                actual_end_time = actual_end_time.time()
                print(actual_end_time)
            else:
                actual_end_time = probable_start_time + dt.timedelta(
                    hours=int(str(office.time_slot_per_patient_time)[1])) + dt.timedelta(minutes=10)
            data = Appointment(doctor_id=doctor_info, patient_id=patient_ID, appointment_date=appointment_date,
                               probable_start_time=probable_start_time, actual_end_time=actual_end_time)
            data.save()
        elif len(appointment_lists) > 0 and availability.end_time > appointment_lists.last().actual_end_time:
            probable_start_time = appointment_lists.last().actual_end_time
            if str(office.time_slot_per_patient_time).endswith("min"):
                actual_end_time = dt.datetime.combine(dt.datetime.strptime(appointment_date, "%Y-%m-%d"),
                                                      probable_start_time) + dt.timedelta(
                    minutes=int(str(office.time_slot_per_patient_time)[:2])) + dt.timedelta(minutes=10)
                actual_end_time = actual_end_time.time()
            else:
                actual_end_time = probable_start_time + dt.timedelta(
                    hours=int(str(office.time_slot_per_patient_time)[1])) + dt.timedelta(minutes=10)
            data = Appointment(doctor_id=doctor_info, patient_id=patient_ID, appointment_date=appointment_date,
                               probable_start_time=probable_start_time, actual_end_time=actual_end_time)
            data.save()
        else:
            messages.error(request, 'All slot is full')
            return render(request, "patient/take_appointment.html",
                          {"doctor_id": doctor_id, "doctor": doctor, "date_list": date_list})

        subject = "Appointment Confirmation"
        message = f"""
               Hello Doctor, \n
               \t Your Appointment is confirmed.
               \nAppointment Details:
               \nDR. {doctor_info.firstname} {doctor_info.lastname}
               \nDate of appointment: {appointment_date} 
               \nTime slot: {probable_start_time}
               \nKindly pay the fee on reception desk RS. {office.first_consultation_fee}.
               \nThis is also show on you dashboard.
               \nI hope we will provide you a better experience. 
               Thank You, 
               Admin
               """
        # emailSend(subject, message, request.user.email)
        return redirect("view_appointment")

    return render(request, "patient/take_appointment.html",
                  {"doctor_id": doctor_id, "doctor": doctor, "date_list": date_list})


@login_required(login_url='/login/')
def view_appointment(request):
    appointmentList = Appointment.objects.filter(patient_id=PatientInfo.objects.get(userid=request.user))
    scheduled = [i for i in appointmentList if i.appointment_date >= dt.date.today()]
    pastAppointments = [i for i in appointmentList if i.appointment_date <= dt.date.today()]
    return render(request, "patient/view_appointment.html",
                  {"scheduled": scheduled, "pastAppointments": pastAppointments})


@login_required(login_url='/login/')
def view_profile(request):
    patient = PatientInfo.objects.get(userid=User.objects.get_by_natural_key(username=request.user))
    return render(request, "patient/patient_profile.html", {"patient": patient})


@login_required(login_url='/login/')
def edit_profile(request):
    patient = PatientInfo.objects.get(userid=User.objects.get_by_natural_key(username=request.user))
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        patient.firstname = firstname
        patient.lastname = lastname
        patient.phone = phone
        patient.gender = gender
        patient.save()
        return redirect("patient_profile")
    return render(request, "patient/update_profile.html", {"patient": patient})


@login_required(login_url='/login/')
def apply_filter(request):
    if request.method == "POST":
        city = request.POST.get('city')
        specialty = request.POST.get('specialty')
        doctors = []
        userid_list = []
        # Filter based on City name
        if specialty == "" or specialty is None:
            for i in Office.objects.filter(city=city):
                userid_list.append(i.userid)
        #  Filter based on Specialty
        elif city == "" or city is None:
            for i in DoctorSpecialization.objects.filter(specialization_id=Specialty.objects.get(name=specialty)):
                userid_list.append(i.userid)
        # Filter based on Specialty and City
        else:
            for i in DoctorSpecialization.objects.filter(specialization_id=Specialty.objects.get(name=specialty)):
                if len(Office.objects.filter(userid=i.userid, city=city)) == 1:
                    userid_list.append(i.userid)

        for i in userid_list:
            try:
                doctorinfo = DoctorInfo.objects.get(userid=i)
                office = Office.objects.get(userid=i)
                doctorAvailability = DoctorAvailability.objects.get(userid=i)
                doctorSpecialization = DoctorSpecialization.objects.get(userid=i)
            except:
                pass
            else:
                data = {'userid': doctorinfo.userid,
                        'firstname': doctorinfo.firstname,
                        'lastname': doctorinfo.lastname,
                        'gender': doctorinfo.gender,
                        'phone': doctorinfo.phone,
                        'address1': office.address1,
                        'address2': office.address2,
                        'city': office.city,
                        'state': office.state,
                        'country': office.country,
                        'zipcode': office.zipcode,
                        'first_consultation_fee': office.first_consultation_fee,
                        'day_of_week': doctorAvailability.day_of_week,
                        'specialty': doctorSpecialization.specialization_id
                        }
                doctors.append(data)
        appointments = [i for i in
                        Appointment.objects.filter(patient_id=PatientInfo.objects.get(
                            userid=User.objegit cts.get_by_natural_key(username=request.user))) if
                        i.appointment_date >= dt.date.today()]
        if len(doctors) >= 30:
            random.shuffle(doctors)
            doctors = doctors[:30]

        cities = set([i.city for i in Office.objects.all() if i.city is not None])
        cities = sorted(list(cities))
        return render(request, 'patient/home.html',
                      {"doctors": doctors, "cities": cities, "specialty": Specialty.objects.all(),
                       "appointments": appointments})
    return redirect("patient_homepage")


@login_required(login_url='/login/')
def cancel_appointment(request, id):
    try:
        appointment = Appointment.objects.get(pk=id)
    except Appointment.DoesNotExist:
        pass
    except:
        pass
    else:
        appointment.delete()
    return redirect("view_appointment")
