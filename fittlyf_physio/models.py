from django.db import models
from django.contrib.auth.models import User


class FittlyfPhysio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='fittlyf_physio')

    def __str__(self):
        return self.user.username
