from django.urls import path

from .views import view_comment, add_comment

urlpatterns = [
    path("", add_comment, name="add_comment"),
    path("view/", view_comment, name="view_comment"),
]
