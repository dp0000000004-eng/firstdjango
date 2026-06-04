from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Comments

# Create your views here.

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'

def commentSection(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("comment_section"))
        else:
            return render(request, "flight/comment.html", {"form":form})
    return render(request, "flight/comment.html", {"form": CommentForm(request.POST), "comments":Comments.objects.all()})

