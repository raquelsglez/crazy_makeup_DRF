# Python imports
import uuid

# Django and DRF imports
from django.db import models

# proof class imports
from utils.models import BaseModel


class CarWorkshop(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    cif = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Worker(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    dni = models.CharField(max_length=20)
    car_workshop = models.ForeignKey(CarWorkshop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Car(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    car_license_plate = models.CharField(max_length=10, unique=True)
    trademark = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.car_license_plate


class Arrangement(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_time = models.DateTimeField()
    worker = models.ManyToManyField(Worker)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.id