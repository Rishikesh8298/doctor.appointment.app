from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from adminApp.models import Specialty
from doctor.models import DoctorInfo, DoctorSpecialization, DoctorAvailability, Office


@login_required(login_url='/login/')
def patient_homepage(request):
    doctorInfo = DoctorInfo.objects.all()
    cities = [i.city for i in Office.objects.all()]
    doctors = []
    for i in doctorInfo:
        try:
            office = Office.objects.get(userid=i.userid)
            doctorAvailability = DoctorAvailability.objects.get(userid=i.userid)
            doctorSpecialization = DoctorSpecialization.objects.get(userid=i.userid)
        except:
            continue
        else:
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
    return render(request, 'patient/home.html',
                  {"doctors": doctors, "cities": cities, "specialty": Specialty.objects.all()})
