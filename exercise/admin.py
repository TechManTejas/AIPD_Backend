from django.contrib import admin
from django.utils.html import format_html

from apid_backend.utilities import export_to_excel
from .models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "sets",
        "description",
        "image",
        "time"
    ]
    actions = [export_to_excel]

    def image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
        else:
            return "No image"
