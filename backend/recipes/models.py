from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=500, null=True)

    REQUIRED_FIELDS = ['name']