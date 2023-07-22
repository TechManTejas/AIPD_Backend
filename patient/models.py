from django.db import models
from django.contrib.auth.models import User
from doctor.models import Doctor
from condition.models import Condition
from fittlyf_physio.models import FittlyfPhysio

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patients')
    fittlyf_physio = models.ForeignKey(FittlyfPhysio, on_delete=models.SET_NULL, related_name='patients', null=True, blank=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='patients')
    duration = models.IntegerField(default=0)
    first_name = models.CharField(max_length=255, default='', null=True, blank=True)
    last_name = models.CharField(max_length=255, default='', null=True, blank=True)

    def __str__(self):
        return self.user.username
