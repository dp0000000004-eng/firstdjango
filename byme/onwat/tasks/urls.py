from django.urls import path
from . import views

urlpatterns = [
    path("task/", views.tasks, name="task"),
    path("task/add", views.add_task, name="add")
]