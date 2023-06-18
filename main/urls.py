from django.urls import path

from .views import home, login, contactus, signup

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('contact-us/', contactus, name='contact_us'),
    path('signup/', signup, name='signup')
]
