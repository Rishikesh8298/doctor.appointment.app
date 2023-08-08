from django.urls import path

from .views import doctor_dashboard, view_profile, change_password, update_profile, view_appointments, \
    today_appointments, upcoming_appointments, change_status, view_patient_profile, unavailability, unavailability_list, \
    view_reason,  search_appointments_by_date

urlpatterns = [
    path('dashboard/', doctor_dashboard, name="doctor_dashboard"),
    path('profile/view/', view_profile, name="view_profile"),
    path('change-password/', change_password, name="change_password"),
    path('profile/edit/', update_profile, name="edit_profile"),
    path('appointments/list/', view_appointments, name="view_appointments"),
    path('appointments/today/', today_appointments, name="today_appointments"),
    path('appointments/future/', upcoming_appointments, name="upcoming_appointments"),
    path('appointments/status/<int:id>/', change_status, name="change_status"),
    path('patient/profile/<str:patient_id>/', view_patient_profile, name="view_patient_profile"),
    path('reason/add/', unavailability, name="unavailability"),
    path('reason/lists/', unavailability_list, name="unavailability_list"),
    path('reason/view/<int:id>', view_reason, name="view_reason"),
    path("search/appointments/", search_appointments_by_date, name="search_appointments_by_date"),
]
