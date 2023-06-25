from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url='/login/')
def admin_dashboard(request):
    return render(request, 'adminApp/home.html')


@login_required(login_url='/login/')
def add_doctor(request):
    return render(request, 'adminApp/add_doctor.html')


@login_required(login_url='/login/')
def view_specialty(request):
    return render(request, "adminApp/specialty_list.html")


@login_required(login_url='/login/')
def add_specialty(request):
    return render(request, "adminApp/add_specialty.html")
