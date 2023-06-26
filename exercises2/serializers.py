# Django and DRF imports
from rest_framework import serializers

# proof class imports
from exercises2.models import Building, Flat, ColorType


class ListBuildingSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = Building
        exclude = ["created_at", "updated_at", "deleted_at", "active"]


class CreateBuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        color_key = representation['color']
        color_value = dict(ColorType.choices)[color_key]
        representation['color'] = color_value
        return representation


class UpdateBuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = "__all__"
        read_only_fields = ["id", "n_floors", "street", "number", "total_flats"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        color_key = representation['color']
        color_value = dict(ColorType.choices)[color_key]
        representation['color'] = color_value
        return representation


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = "__all__"


class UpdateFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = "__all__"
        read_only_fields = ["floor", "letter", "square_meter"]
