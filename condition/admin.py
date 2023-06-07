from django.contrib import admin

from apid_backend.utilities import export_to_excel
from .models import Condition


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    actions = [export_to_excel]
