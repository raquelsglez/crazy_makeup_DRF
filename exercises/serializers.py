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
            anchura=validated_data["anchura"],
            altura=validated_data["altura"],
            color=validated_data["color"],
            nombre=validated_data["nombre"],
            marca=validated_data["marca"]
        )
        nevera.save()
        return nevera

    # def update(self, instance, validated_data):  # PATCH/PUT
    #
    #     instance.anchura = validated_data.get("anchura")
    #     instance.color = validated_data.get("color", "negro")
    #
    #
    #     instance.save(update_fields=["anchura", "color"])
    #
    #     return instance
