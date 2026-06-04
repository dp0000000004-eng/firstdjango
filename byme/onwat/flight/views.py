from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UserComment, User

# Create your views here.
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = '__all__'

def commentSection(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("comment_section"))
        else:
            form = CommentForm()
    return render(request, "flight/comment.html", {"form": CommentForm(request.POST), "comments":UserComment.objects.all(), "users":User.objects.all()})



def user_section(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse("comment_section"))
        else:
            user_form = UserForm()
    return render(request, "flight/user.html", {"user_form":UserForm(request.POST)})
