from django.db import models
from django.contrib.auth.models import User

from company.models import Company

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company', default=1)

    def __str__(self):
        return self.user.username
