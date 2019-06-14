from django.db import models
from django.urls import reverse

class Bug(models.Model):
    name = models.CharField(max_length=100)
    type_bug = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
# Create your models here.
