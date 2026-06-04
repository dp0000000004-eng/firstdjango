from django.db import models

# Create your models here.

class Comments(models.Model):
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.comment}"