from django.contrib import admin

from apid_backend.utilities import export_to_excel
from .models import Doctor
from patient.models import Patient

class PatientInline(admin.TabularInline):
    model = Patient
    extra = 0


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    inlines = [PatientInline]
    list_display = [
        "id",
        "user",
        "company"
    ]
    actions = [export_to_excel]
