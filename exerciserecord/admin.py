from django.contrib import admin
from .models import ExerciseRecord


@admin.register(ExerciseRecord)
class ExerciseRecordAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "patient",
        "exercise",
        "date",
        'videoURL'
    ]
