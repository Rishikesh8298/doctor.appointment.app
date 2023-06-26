from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

from adminApp.models import Specialty
from patient.models import PatientInfo


class DoctorInfo(models.Model):
    userid = models.ForeignKey(User, blank=False, on_delete=CASCADE, db_column="username")
    firstname = models.CharField(max_length=30, db_column="first_name")
    lastname = models.CharField(max_length=30, db_column="last_name")
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=8)
    practicing_year = models.DateField(null=True)
    professional_statement = models.TextField(null=True)


class Qualification(models.Model):
    """This models stores details about doctor's education and professional qualification."""
    userid = models.ForeignKey(User, blank=False, on_delete=CASCADE, db_column="username")
    name = models.CharField(max_length=200, db_column="qualification_name")
    institute_name = models.CharField(max_length=200)
    passing_year = models.DateField()


class Office(models.Model):
    """The Office models holds information about the outpatient department of their office"""
    userid = models.ForeignKey(User, blank=False, on_delete=CASCADE, db_column="username")
    office_name = models.CharField(max_length=40)
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)
    time_slot_per_patient_time = models.CharField(max_length=20)
    first_consultation_fee = models.CharField(max_length=20)
    followup_consultation_fee = models.CharField(max_length=20)


class DoctorSpecialization(models.Model):
    userid = models.ForeignKey(User, blank=False, on_delete=CASCADE, db_column="username")
    specialization_id = models.ForeignKey(Specialty, blank=False, on_delete=CASCADE)


class OfficeDoctorAvailability(models.Model):
    """This models stores doctor's patient visiting time in terms of timeslots"""
    office_id = models.ForeignKey(Office, blank=False, on_delete=CASCADE)
    day_of_week = models.CharField(max_length=15)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.CharField(max_length=3)


class Appointment(models.Model):
    """This models holds appointment Details for patients."""
    office_id = models.ForeignKey(Office, blank=False, on_delete=CASCADE)
    patient_id = models.ForeignKey(PatientInfo, blank=False, on_delete=CASCADE)
    probable_start_time = models.TimeField()
    actual_end_time = models.TimeField()
    appointment_date = models.DateField()
