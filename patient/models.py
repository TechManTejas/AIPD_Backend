from django.db import models
from doctor.models import Doctor
from condition.models import Condition


class Patient(models.Model):
    name = models.CharField(max_length=255)
    phone_no = models.BigIntegerField(unique=True)
    code = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
