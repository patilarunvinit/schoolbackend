from django.contrib import admin
from .models import attandmodN

# Register your models here.
class attandForSAdmin(admin.ModelAdmin):
    list_display =("teacher_name","name", "class_div", "roll_no", "date")


admin.site.register(attandmodN, attandForSAdmin)