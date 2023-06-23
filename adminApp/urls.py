from django.urls import path

from .views import admin_dashboard, add_doctor

urlpatterns = [
    path('dashboard/', admin_dashboard, name="admin_dashboard"),
    path('add-doctor/', add_doctor, name="add_doctor"),
]
