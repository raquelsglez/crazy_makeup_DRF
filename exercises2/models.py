# Python imports
import uuid

# Django and DRF imports
from django.db import models
from authentication.models import User

# proof class imports
from utils.models import BaseModel


class ColorType(models.TextChoices):
    BLUE = 'A', 'Azul'
    YELLOW = 'Am', 'Amarillo'
    BLACK = 'N', 'Negro'
    WHITE = 'B', 'Blanco'
    ROSA = 'R', 'Rosa'

    @classmethod
    def get_all_choices(cls):
        return {choice.value: choice.label for choice in cls}


class Building(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    n_floors = models.IntegerField()
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    color = models.CharField(max_length=50, choices=ColorType.choices)
    total_flats = models.IntegerField()

    class Meta:
        verbose_name = "Building"
        verbose_name_plural = "Buildings"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Building {self.street} {self.number}"


class Flat(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    square_meter = models.DecimalField(max_digits=10, decimal_places=2)
    n_rooms = models.IntegerField()
    n_bathrooms = models.IntegerField()
    floor = models.IntegerField()
    letter = models.CharField(max_length=5)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Flat"
        verbose_name_plural = "Flats"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Flat {self.floor} {self.letter} - Building {self.id}"