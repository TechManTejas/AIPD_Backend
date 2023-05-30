from django.contrib import admin
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
