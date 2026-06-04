from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class TaskForm(forms.Form):
    task = forms.CharField(max_length=64)
    priority = forms.IntegerField(min_value=1, max_value=10)

list_of_tasks = []

def tasks(request):
    return render(request, "tasks/tasks.html", {"tasks":list_of_tasks})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            list_of_tasks.append(task)
            return HttpResponseRedirect(reverse("task"))
        else:
            return render(request, "tasks/add.html",{"form":form})
    return render(request, "tasks/add.html", {"form":TaskForm()})