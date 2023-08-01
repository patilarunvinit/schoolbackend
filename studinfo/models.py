from django.db import models

# Create your models here.


class sinfo(models.Model):
    username = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    mother = models.CharField(max_length=15)
    class_div = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=5)
    reg_no = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=13)
    b_day = models.DateField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, verbose_name="")


    objects = models.Manager()


 ##### FOR TEACHER ATTENDANCE #####
    def option1(self):
        return False

    def teacher_name1(self):
        return "dsadas"

    def date1(self):
        return ""