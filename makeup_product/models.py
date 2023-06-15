# Python imports
import uuid

# Django and DRF imports
from django.db import models
from authentication.models import User

# proof class imports
from utils.models import BaseModel


class ColorType(models.TextChoices):
    RED = 'R', 'Rojo'
    BLUE = 'A', 'Azul'
    YELLOW = 'Am', 'Amarillo'
    BLACK = 'N', 'Negro'
    SILVER = 'P', 'Plateado'
    WHITE = 'B', 'Blanco'
    GOLDEN = 'D', 'Dorado'

    @classmethod
    def get_all_choices(cls):
        return {choice.value: choice.label for choice in cls}


class MakeupProduct(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.IntegerField()  # int
    name = models.CharField(max_length=100)  # string
    trademark = models.CharField(max_length=50)
    color = models.CharField(max_length=50, choices=ColorType.choices)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "MakeupProduct"
        verbose_name_plural = "MakeupProducts"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}"
