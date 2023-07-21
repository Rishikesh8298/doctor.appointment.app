from django.urls import path

from .views import admin_dashboard, add_doctor, view_specialty, add_specialty, password_sent, import_doctor_data, \
    doctor_list

urlpatterns = [
    path('dashboard/', admin_dashboard, name="admin_dashboard"),
    path('doctor-list', doctor_list, name="doctor_list"),
    path('add-doctor/', add_doctor, name="add_doctor"),
    path('view-specialty/', view_specialty, name="view_specialty"),
    path('add-specialty/', add_specialty, name="add_specialty"),
    path('upload-doctor/', import_doctor_data, name="import_doctor_data"),
    path('<str:userid>/', password_sent, name="password_sent"),
]
