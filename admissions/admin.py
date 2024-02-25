from django.contrib import admin
from admissions.models import ManagementStudent
from import_export.admin import ExportActionModelAdmin

# Register your models here.

@admin.register(ManagementStudent)
class AdmissionAdmin(ExportActionModelAdmin):
    list_display = ("full_name", )