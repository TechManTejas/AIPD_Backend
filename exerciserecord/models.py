from django.db import models
from patient.models import Patient
from exercise.models import Exercise

class ExerciseRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='exercise_records')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='exercise_records')
    date = models.DateField()
    videoURL = models.URLField(default=None)

    def __str__(self):
        return f'{self.patient} - {self.exercise} - {self.date}'
