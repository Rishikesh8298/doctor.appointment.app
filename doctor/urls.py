from django.urls import path

from .views import doctor_dashboard, view_profile, change_password, update_profile

urlpatterns = [
    path('dashboard/', doctor_dashboard, name="doctor_dashboard"),
    path('view-profile/', view_profile, name="view_profile"),
    path('change-password/', change_password, name="change_password"),
    path('edit-profile/', update_profile, name="edit_profile"),
]
