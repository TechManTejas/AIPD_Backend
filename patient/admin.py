from django.contrib import admin

from apid_backend.utilities import export_to_excel
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "doctor",
        "condition",
        "duration"
    ]
    actions = [export_to_excel]
