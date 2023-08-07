from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logos/')
    color_theme = models.JSONField(blank=True, default=dict)
    google_business_review_link = models.URLField(blank=True)

    def __str__(self):
        return self.name
