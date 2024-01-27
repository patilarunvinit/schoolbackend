from django.contrib import admin
from .models import contactmodel

# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display =("name", "email", "massage")

admin.site.register(contactmodel, contactAdmin)
