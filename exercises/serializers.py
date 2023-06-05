# Django and DRF imports
from rest_framework import serializers

# proof class imports
from exercises.models import Television, Nevera


class TelevisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Television
        fields = "__all__"

    def create(self, validated_data):
        television = Television(**validated_data)
        television.save()
        return television

    def update(self, instance, validated_data):  # PUT

        instance.pulgadas = validated_data["pulgadas"]
        instance.numero_de_serie = validated_data["numero_de_serie"]

        instance.save(update_fields=["pulgadas", "numero_de_serie"])
        return instance


class NeveraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nevera
        fields = "__all__"

    def create(self, validated_data):
        nevera = Nevera(
            anchura="5",
            altura="2",
            color="negro"
        )
        nevera.save()
        return nevera

    def update(self, instance, validated_data):  # PATCH

        instance.altura = validated_data.get("altura")
        instance.color = validated_data["color"]
        instance.anchura = validated_data["anchura"]

        instance.save(update_fields=["anchura", "altura"])
        return instance
