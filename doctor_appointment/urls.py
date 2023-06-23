from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('superuser/', admin.site.urls),
    path('', include('main.urls')),
    path('admin/', include('adminApp.urls')),
    path('patient/', include('patient.urls')),
    path('doctor/', include('doctor.urls')),
    path('comment/', include('comment.urls')),
]
