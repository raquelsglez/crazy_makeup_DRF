# Django and DRF imports
from rest_framework import serializers
from authentication.serializers import UserProfileSerializer

# proof class imports
from .models import MakeupProduct, ColorType


class ListMakeupProductSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')
    user = UserProfileSerializer()

    class Meta:
        model = MakeupProduct
        exclude = ["created_at", "updated_at", "deleted_at", "active"]


class ListProfileMakeupProductSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')
    user = UserProfileSerializer()

    class Meta:
        model = MakeupProduct
        fields = "__all__"


class CreateMakeupProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = MakeupProduct
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        color_key = representation['color']
        color_value = dict(ColorType.choices)[color_key]
        representation['color'] = color_value
        return representation


class UpdateMakeupProductSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = MakeupProduct
        fields = "__all__"
        read_only_fields = ["id", "color", "trademark"]
