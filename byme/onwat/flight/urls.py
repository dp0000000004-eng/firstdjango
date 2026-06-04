from django.urls import path
from . import views

urlpatterns = [
    path("", views.commentSection, name="comment_section"),
]