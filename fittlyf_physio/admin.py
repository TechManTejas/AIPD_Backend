from django.contrib import admin
from apid_backend.utilities import export_to_excel
from .models import FittlyfPhysio
from patient.models import Patient


@admin.register(FittlyfPhysio)
class FittlyfPhysioAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user"
    ]
    actions = [export_to_excel]