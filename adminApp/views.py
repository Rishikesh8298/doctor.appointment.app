from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from doctor.models import DoctorInfo, DoctorSpecialization, Office, Qualification, DoctorAvailability
from module.email_send import emailSend
from module.pagination import create_pagination
from module.password_generator import password_generator
from .models import Specialty


# Create your views here.
@login_required(login_url='/login/')
def admin_dashboard(request):
    return render(request, 'adminApp/dashboard.html')


@login_required(login_url='/login/')
def doctor_list(request):
    doctors = DoctorInfo.objects.all().order_by('-pk')
    page = request.GET.get('page')
    main = create_pagination(main=doctors, no=30, page=page)
    return render(request, 'adminApp/doctor_list.html', {"main": main})


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
    emailSend(subject, message, userinfo.email)
    doc = DoctorInfo.objects.get(userid=userinfo)
    doc.is_password_sent = True
    doc.save()
    return redirect("doctor_list")


@login_required(login_url='/login/')
def import_doctor_data(request):
    if request.method == "POST":
        csv_file = request.FILES['file']
        if not csv_file.name.endswith(".csv"):
            error = "Please Input csv file"
            messages.error(request, error)

        if csv_file.multiple_chunks():
            error = "Please Input CSV file"
            messages.error(request, error)

        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:
            fields = line.split(",")
            try:
                if fields[3] == "Gender":
                    pass
                else:
                    firstname = fields[0]
                    lastname = fields[2]
                    gender = fields[3]
                    address1 = fields[4]
                    address2 = fields[5]
                    city = fields[6]
                    country = fields[7]
                    state = fields[8]
                    zipcode = fields[9]
                    phone = fields[10]
                    specialty = fields[11]
                    email = fields[12]
                    availability = fields[13]
                    time_slot = fields[14]
                    fee = fields[15]
                    follow_up = fields[16]

                    username = email[:email.rindex("@")]
                    if gender == "M":
                        gender = "Male"
                    else:
                        gender = "Female"

                    User.objects.create_user(username=username, email=email, password=password_generator())
                    specialty = DoctorSpecialization(userid=User.objects.get(username=username),
                                                     specialization_id=Specialty.objects.get(name=specialty))
                    specialty.save()
                    doctor = DoctorInfo(userid=User.objects.get(username=username), firstname=firstname,
                                        lastname=lastname,
                                        phone=phone, gender=gender)
                    doctor.save()

                    office = Office(userid=User.objects.get(username=username), address1=address1,
                                    address2=address2, city=city, state=state, country=country, zipcode=zipcode,
                                    time_slot_per_patient_time=time_slot, first_consultation_fee=fee,
                                    followup_consultation_fee=follow_up)
                    office.save()

                    qualification = Qualification(userid=User.objects.get(username=username))
                    qualification.save()
                    doctorAvailability = DoctorAvailability(userid=User.objects.get(username=username),
                                                            day_of_week=availability, start_time="09:30:00",
                                                            end_time="21:30:00")
                    doctorAvailability.save()

            except:
                print("Okkay")
    return render(request, "adminApp/import_doctor.html")
