from django.db import models


class Exercise(models.Model):
    name = models.CharField(default='', max_length=255)
    image = models.ImageField(default="media/exercises/default_exercise.jpg", upload_to="exercises")
    description = models.TextField(default='', blank=True, null=True)
    grade_1_details = models.TextField(default='', blank=True, null=True)
    grade_2_details = models.TextField(default='', blank=True, null=True)
    grade_3_details = models.TextField(default='', blank=True, null=True)
    video_link = models.CharField(default='', blank=True,  max_length=255)

    def __str__(self):
        return self.name
