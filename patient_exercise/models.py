from django.db import models
from patient.models import Patient
from exercise.models import Exercise


class PatientExercise(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField(default=5)

    # Other fields and methods

    def __str__(self):
        return f"{self.patient} - {self.exercise}"
