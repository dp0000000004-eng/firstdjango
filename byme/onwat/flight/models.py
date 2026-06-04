from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class UserComment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}:- {self.comment}"