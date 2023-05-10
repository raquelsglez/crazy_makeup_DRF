# Django and DRF imports
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()  # para obtener todos los productos y poder filtrarlos

    class Meta:
        abstract = True  # para que no se cree una tabla
