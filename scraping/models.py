from django.db import models

class City(models.Model):
    name = models.CharField(max_Length=50)
    slug = models.CharField(max_Length=50, blank=True)
