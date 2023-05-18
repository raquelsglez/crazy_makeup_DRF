# Django and DRF imports
from rest_framework import serializers

# proof class imports
from .models import MakeupProduct


class MakeupProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = MakeupProduct
        fields = "__all__"


class UpdateMakeupProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeupProduct
        fields = "__all__"
        read_only_fields = ["id", "color", "trademark"]
