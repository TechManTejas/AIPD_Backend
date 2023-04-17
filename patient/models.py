from django.db import models
from django.contrib.auth.models import User
from doctor.models import Doctor
from condition.models import Condition

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patients')
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='patients')
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
