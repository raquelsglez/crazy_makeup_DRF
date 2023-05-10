# Python imports
import uuid

# Django and DRF imports
from django.db import models

# proof class imports
from utils.models import TimestampedModel


class MakeupProduct(TimestampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.IntegerField()  # int
    name = models.CharField(max_length=255)  # string
    trademark = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    price = models.IntegerField()

    class Meta:
        verbose_name = "MakeupProduct"
        verbose_name_plural = "MakeupProducts"

    def __str__(self):
        return f"{self.name}"
