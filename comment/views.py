from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment


# Create your views here.
def add_comment(request):
    return redirect("contactus")

@login_required(login_url='/login/')
def view_comment(request):
    all_comment = Comment.objects.all().order_by("-pk")
    return render(request, "comment/view_comment.html", {"list": all_comment})
