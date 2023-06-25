from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/login/')
def patient_homepage(request):
    return render(request, 'patient/home.html')
