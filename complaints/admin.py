from django.contrib import admin
from .models import CompModel

# Register your models here.
class complaintAdmin(admin.ModelAdmin):
    list_display =("teacher_name", "name", "class_div", "date", "complaint", "mobile_no", "complaint_date1")


admin.site.register(CompModel, complaintAdmin)
