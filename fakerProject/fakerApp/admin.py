from django.contrib import admin
from fakerApp.models import student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    l=["name","roll","marks","dob","email"]
admin.site.register(student,studentAdmin)
