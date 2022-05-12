from django.db import models


class Hospital(models.Model):
    name = models.CharField()
    distance = models.CharField()
    lat = models.CharField()
    lon = models.CharField()
    link = models.CharField()

