from django.db import models

# Create your models here.
class contactmodel(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=30)
    massage = models.CharField(max_length=500)

    objects = models.Manager()
