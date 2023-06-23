from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class PatientInfo(models.Model):
    userid = models.ForeignKey(User, blank=False, on_delete=CASCADE, db_column="username")
    firstname = models.CharField(max_length=30, db_column="first_name")
    lastname = models.CharField(max_length=30, db_column="last_name")
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=8)

    def __str__(self):
        return self.firstname + self.lastname + self.userid
