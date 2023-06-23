from django.urls import path

from .views import patient_homepage

urlpatterns = [
    path('dashboard/', patient_homepage, name="patient_homepage"),
]
