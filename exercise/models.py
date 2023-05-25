from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.IntegerField(default=2)
    description = models.TextField()
    image = models.ImageField(upload_to='exercise_images/')
    link = models.URLField(blank=True)
    data = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.name
