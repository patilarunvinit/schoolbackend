from django.contrib import admin
from .models import tinfo

# Register your models here.
class teachinfoAdmin(admin.ModelAdmin):
    list_display =("username","name", "mother", "employe_id", "mobile_no","b_day","address","image")


admin.site.register(tinfo, teachinfoAdmin)
