from django.urls import path

from .views import admin_dashboard, add_doctor, view_specialty, add_specialty

urlpatterns = [
    path('dashboard/', admin_dashboard, name="admin_dashboard"),
    path('add-doctor/', add_doctor, name="add_doctor"),
    path('view_specialty/', view_specialty, name="view_specialty"),
    path('add_specialty/', add_specialty, name="add_specialty"),
]
