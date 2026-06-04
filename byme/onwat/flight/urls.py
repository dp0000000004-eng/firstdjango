from django.urls import path
from . import views

urlpatterns = [
    path("comment/", views.commentSection, name="comment_section"),
    path("", views.user_section, name="user_section")
]