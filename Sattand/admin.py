from django.contrib import admin
from .models import attandmodN
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class attandForSAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display =("teacher_name","name", "class_div", "roll_no", "date")


admin.site.register(attandmodN, attandForSAdmin)