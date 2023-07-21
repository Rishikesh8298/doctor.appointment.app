from django.urls import path

from .views import doctor_dashboard, view_profile, change_password, update_profile, view_appointments, \
    today_appointments

urlpatterns = [
    path('dashboard/', doctor_dashboard, name="doctor_dashboard"),
    path('profile/view/', view_profile, name="view_profile"),
    path('change-password/', change_password, name="change_password"),
    path('profile/edit/', update_profile, name="edit_profile"),
    path('appointment/list/', view_appointments, name="view_appointments"),
    path('appointment/today/', today_appointments, name="today_appointments"),
]
