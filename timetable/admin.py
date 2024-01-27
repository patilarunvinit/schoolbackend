from django.contrib import admin
from .models import tt
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class timetableAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display =("stand","time","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")


admin.site.register(tt, timetableAdmin)
