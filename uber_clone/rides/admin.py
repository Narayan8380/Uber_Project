from django.contrib import admin
from . models import note,rider,driver

# Register your models here.
admin.site.register(note)
admin.site.register(rider)
admin.site.register(driver)