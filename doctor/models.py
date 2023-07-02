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
    professional_statement = models.TextField(default=None, null=True)
    is_password_sent = models.BooleanField(default=False)


class Qualification(models.Model):
    """This models stores details about doctor's education and professional qualification."""
    userid = models.ForeignKey(User, blank=False, on_delete=CASCADE, db_column="username")
    name = models.CharField(max_length=200, db_column="qualification_name", default=None, null=True)
    institute_name = models.CharField(max_length=200, default=None, null=True)
    passing_year = models.DateField(null=True)


class Office(models.Model):
    """The Office models holds information about the outpatient department of their office"""
    userid = models.ForeignKey(User, blank=False, on_delete=CASCADE, db_column="username")
    office_name = models.CharField(max_length=40, default=None, null=True)
    address1 = models.TextField(default=None, null=True)
    address2 = models.TextField(default=None, null=True)
    city = models.CharField(max_length=40, default=None, null=True)
    state = models.CharField(max_length=40, default=None, null=True)
    country = models.CharField(max_length=20, default=None, null=True)
    zipcode = models.CharField(max_length=10, default=None, null=True)
    time_slot_per_patient_time = models.CharField(max_length=20, default=None, null=True)
    first_consultation_fee = models.CharField(max_length=20, default=None, null=True)
    followup_consultation_fee = models.CharField(max_length=20, default=None, null=True)


class DoctorSpecialization(models.Model):
    userid = models.ForeignKey(User, blank=False, on_delete=CASCADE, db_column="username")
    specialization_id = models.ForeignKey(Specialty, blank=False, on_delete=CASCADE)


class DoctorAvailability(models.Model):
    """This models stores doctor's patient visiting time in terms of timeslots"""
    userid = models.ForeignKey(User, blank=False, on_delete=CASCADE, db_column="username")
    day_of_week = models.CharField(max_length=15, default=None, null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)


class Appointment(models.Model):
    """This models holds appointment Details for patients."""
    doctor_id = models.ForeignKey(DoctorInfo, blank=False, on_delete=CASCADE, null=False)
    patient_id = models.ForeignKey(PatientInfo, blank=False, on_delete=CASCADE, null=False)
    probable_start_time = models.TimeField()
    actual_end_time = models.TimeField()
    appointment_date = models.DateField()
