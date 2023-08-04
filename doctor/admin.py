from django.contrib import admin

from .models import Office, DoctorAvailability, Appointment, DoctorInfo, DoctorSpecialization, Qualification, \
    Unavailability

# Register your models here.

admin.site.register(DoctorInfo)
admin.site.register(Qualification)
admin.site.register(DoctorSpecialization)
admin.site.register(Office)
admin.site.register(DoctorAvailability)
admin.site.register(Appointment)
admin.site.register(Unavailability)
