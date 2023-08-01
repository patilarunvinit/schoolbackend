from django.db import models

# Create your models here.


class attandmodN(models.Model):
    teacher_name = models.CharField(max_length=60,null=True)
    name = models.CharField(max_length=60,null=True)
    class_div = models.CharField(max_length=10,null=True)
    roll_no = models.CharField(max_length=5,null=True)
    option = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateField(null=True, blank=True)

    objects = models.Manager()
