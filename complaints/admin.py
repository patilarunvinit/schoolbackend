from django.contrib import admin
from .models import CompModel
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class complaintAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display =("teacher_name", "name", "class_div", "date", "complaint", "mobile_no", "complaint_date1")


admin.site.register(CompModel, complaintAdmin)
