from django.contrib import admin
from django.utils import timezone
from datetime import datetime, timedelta
from apid_backend.utilities import export_to_excel
from patient_exercise.models import PatientExercise
from .models import ExerciseRecord


class DateRangeFilter(admin.SimpleListFilter):
    title = 'Date'
    parameter_name = 'date'

    def lookups(self, request, model_admin):
        return (
            ('today', 'Today'),
            ('yesterday', 'Yesterday'),
            ('past_7_days', 'Past 7 Days'),
            ('this_month', 'This Month'),
            ('this_year', 'This Year'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'today':
            today = timezone.now().date()
            return queryset.filter(date__gte=today, date__lt=today + timedelta(days=1))
        elif self.value() == 'yesterday':
            yesterday = timezone.now().date() - timedelta(days=1)
            return queryset.filter(date__gte=yesterday, date__lt=yesterday + timedelta(days=1))
        elif self.value() == 'past_7_days':
            seven_days_ago = timezone.now().date() - timedelta(days=7)
            return queryset.filter(date__gte=seven_days_ago, date__lt=timezone.now().date() + timedelta(days=1))
        elif self.value() == 'this_month':
            start_of_month = timezone.now().replace(
                day=1, hour=0, minute=0, second=0, microsecond=0)
            return queryset.filter(date__gte=start_of_month, date__lt=timezone.now() + timedelta(days=1))
        elif self.value() == 'this_year':
            start_of_year = timezone.now().replace(month=1, day=1, hour=0,
                                                   minute=0, second=0, microsecond=0)
            return queryset.filter(date__gte=start_of_year, date__lt=timezone.now() + timedelta(days=1))


@admin.register(ExerciseRecord)
class ExerciseRecordAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "review",
        "patient",
        "exercise",
        "get_sets",
        "get_reps",
        "date",
        'video'
    ]
    list_filter = [
        "review",
        "patient",
        "exercise",
        DateRangeFilter,
    ]
    actions = [export_to_excel]

    def get_sets(self, obj):
        patient_exercise = PatientExercise.objects.get(
            patient=obj.patient.id,
            exercise=obj.exercise
        )
        return patient_exercise.sets
    get_sets.short_description = 'sets'

    def get_reps(self, obj):
        patient_exercise = PatientExercise.objects.get(
            patient=obj.patient.id,
            exercise=obj.exercise
        )
        return patient_exercise.reps
    get_reps.short_description = 'reps'
