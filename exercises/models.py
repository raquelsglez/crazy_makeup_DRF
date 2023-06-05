# Python imports
import uuid

# Django and DRF imports
from django.db import models

# proof class imports
from utils.models import BaseModel


class Television(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pulgadas = models.PositiveIntegerField()
    numero_de_serie = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Television {self.numero_de_serie}"


class Nevera(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    anchura = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"Nevera {self.color}"
