from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField()
    dob = models.DateField()
    location = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name
