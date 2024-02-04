from django.contrib import admin
from .models import sinfo
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class studinfoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display =("username","name", "mother", "class_div", "roll_no", "reg_no", "mobile_no","b_day","address","image")


admin.site.register(sinfo, studinfoAdmin)
