from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Comment


# Create your views here.
def add_comment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('Comments')
        add_data = Comment(name=name, email=email, comment=comment)
        add_data.save()
        messages.success(request, "Successfully posted to Admin.")
    return redirect("contact_us")


@login_required(login_url='/login/')
def view_comment(request):
    all_comment = Comment.objects.all().order_by("-pk")
    return render(request, "comment/view_comment.html", {"list": all_comment})
