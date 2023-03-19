from django.db import models
from exercise.models import Exercise

class Condition(models.Model):
    name = models.CharField(default='', max_length=255)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.name
