from django.urls import path

from .views import home, userlogin, contactus, signup, userLogout

urlpatterns = [
    path('', home, name='home'),
    path('login/', userlogin, name='login'),
    path('contact-us/', contactus, name='contact_us'),
    path('signup/', signup, name='signup'),
    path('logout/', userLogout,name='logout'),
]
