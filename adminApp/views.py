from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login/')
def admin_dashboard(request):
    return render(request, 'admin/home.html')

