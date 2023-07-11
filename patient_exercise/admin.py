from django.contrib import admin

from apid_backend.utilities import export_to_excel
from .models import PatientExercise


@admin.register(PatientExercise)
class PatientExerciseAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "patient",
        "exercise",
        "sets",
        "reps"
    ]
    list_filter = [
        "patient",
        "exercise"
    ]
    actions = [export_to_excel]
