import datetime

from django.test import TestCase, Client

from doctor.models import DoctorInfo, Appointment
from doctor.models import User
from patient.models import PatientInfo


class PatientTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.patient = {
            "username": "patient1",
            "password": "password",
        }
        User.objects.create_user(**self.patient)
        PatientInfo.objects.create(userid=User.objects.get_by_natural_key(username=self.patient["username"]))
        self.email = "morton.jon68@gmail.com"
        self.data = {
            "firstname": "Jon",
            "lastname": "Morton",
            "phone": "7886451236",
            "gender": "Male",
        }
        self.credential = {
            "username": self.email[:str(self.email).rindex("@")],
            "password": "password",
        }
        User.objects.create_user(**self.credential)
        DoctorInfo.objects.create(userid=User.objects.get_by_natural_key(self.credential["username"]), **self.data)

    def test_take_appointment(self):
        response = self.client.post("/login/", self.patient, follow=True)
        Appointment.objects.create(
            doctor_id=DoctorInfo.objects.get(
                userid=User.objects.get_by_natural_key(username=self.credential["username"])),
            patient_id=PatientInfo.objects.get(
                userid=User.objects.get_by_natural_key(username=self.patient["username"])),
            appointment_date=datetime.date.today() + datetime.timedelta(2)
        )
        self.assertTrue(Appointment.objects.filter(patient_id=PatientInfo.objects.get(
            userid=User.objects.get_by_natural_key(username=self.patient["username"]))) != 0)
        self.assertTrue(response.context['user'].is_active)

    def appointment_booking(self):
        Appointment.objects.create(
            doctor_id=DoctorInfo.objects.get(
                userid=User.objects.get_by_natural_key(username=self.credential["username"])),
            patient_id=PatientInfo.objects.get(
                userid=User.objects.get_by_natural_key(username=self.patient["username"])),
            appointment_date=datetime.date.today() + datetime.timedelta(2)
        )

    def test_cancel_appointment(self):
        response = self.client.post("/login/", self.patient, follow=True)
        self.appointment_booking()
        appointment = Appointment.objects.get(
            doctor_id=DoctorInfo.objects.get(
                userid=User.objects.get_by_natural_key(username=self.credential["username"])),
            patient_id=PatientInfo.objects.get(
                userid=User.objects.get_by_natural_key(username=self.patient["username"])),
            appointment_date=datetime.date.today() + datetime.timedelta(2),
        )
        appointment.status = "Cancel"
        appointment.save()
        self.assertTrue(Appointment.objects.filter(patient_id=PatientInfo.objects.get(
            userid=User.objects.get_by_natural_key(username=self.patient["username"]))) != 0)

        # self.assertEqual(cancel.status, "Cancel")
