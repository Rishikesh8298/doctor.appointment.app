from django.urls import path

from .views import patient_homepage, take_appointment, view_appointment, view_profile, edit_profile, apply_filter, \
    cancel_appointment, view_doctor, change_password_of_patient

urlpatterns = [
    path('dashboard/', patient_homepage, name="patient_homepage"),
    path('booking/<str:doctor_id>/', take_appointment, name="take_appointment"),
    path('appointments/list/', view_appointment, name="view_appointment"),
    path('profile/view/', view_profile, name="patient_profile"),
    path('profile/edit/', edit_profile, name="patient_edit_profile"),
    path('apply/filter/', apply_filter, name="apply_filter"),
    path('appointment/cancel/<int:id>/', cancel_appointment, name="cancel_appointment"),
    path('view/doctor/<str:id>/', view_doctor, name="view_doctor"),
    path('change/password/', change_password_of_patient, name="change_password_of_patient"),
]
