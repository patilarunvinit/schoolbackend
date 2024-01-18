from django.db import models
from django.utils import timezone


# Create your models here.

class CompModel(models.Model):
    teacher_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    class_div = models.CharField(max_length=10)
    date = models.DateField(blank=True)
    complaint = models.CharField(max_length=500)

    objects = models.Manager()