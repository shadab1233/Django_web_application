from django.contrib import admin

# Register your models here.
from .models import Students
@admin.register(Students)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
