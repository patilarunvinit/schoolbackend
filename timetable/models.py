from django.db import models

# Create your models here.


class tt(models.Model):
    stand = models.CharField(max_length=50)
    time = models.CharField(max_length=100)
    Monday = models.CharField(max_length=50)
    Tuesday = models.CharField(max_length=50)
    Wednesday = models.CharField(max_length=50)
    Thursday = models.CharField(max_length=50)
    Friday = models.CharField(max_length=50)
    Saturday = models.CharField(max_length=50)


    objects = models.Manager()