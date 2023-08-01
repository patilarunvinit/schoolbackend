
from django.db import models




class tinfo(models.Model):
    username = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    mother = models.CharField(max_length=15)
    employe_id = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=13)
    b_day = models.DateField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, verbose_name="")


    objects = models.Manager()