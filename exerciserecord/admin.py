from django.contrib import admin

from apid_backend.utilities import export_to_excel
from .models import ExerciseRecord


@admin.register(ExerciseRecord)
class ExerciseRecordAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "patient",
        "exercise",
        "date",
        'video'
    ]
    actions = [export_to_excel]
