from django.db import models
from exercise.models import Exercise

class Condition(models.Model):
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercise, related_name='conditions', blank=True)

    def __str__(self):
        return self.name
