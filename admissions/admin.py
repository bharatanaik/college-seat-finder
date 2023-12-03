from django.contrib import admin
from admissions.models import ManagementStudent
# Register your models here.

@admin.register(ManagementStudent)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ("full_name", )