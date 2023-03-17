from django.db import models

class Exercise(models.Model):
    name = models.CharField(default='', max_length=255)
    image = models.ImageField(default="media/exercises/default_exercise.jpg", upload_to="exercises")
    video_link = models.CharField(blank=True, default='', max_length=255)

    def __str__(self):
        return self.name
