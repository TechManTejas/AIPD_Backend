from django.db import models
from django.contrib.auth.models import AbstractUser
from doctor.models import Doctor
from condition.models import Condition


class User(AbstractUser):
    is_patient = models.BooleanField(default=False, null=True, blank=True)
    phonenumber = models.BigIntegerField(unique=True, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
