# Django and DRF imports
from rest_framework import serializers

# proof class imports
from activities.models import CarWorkshop, Worker, Car, Arrangement


class CarWorkshopSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarWorkshop
        fields = "__all__"


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = "__all__"


class RetrieveCarWorkshopSerializer(serializers.ModelSerializer):

    workers = serializers.SerializerMethodField()

    class Meta:
        model = CarWorkshop
        fields = "__all__"

    def get_workers(self, obj):
        workers = Worker.objects.filter(car_workshop=obj)
        return WorkerSerializer(workers, many=True).data


class RetrieveWorkerSerializer(serializers.ModelSerializer):

    car_workshop = CarWorkshopSerializer()

    class Meta:
        model = Worker
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"


class ListArrangementSerializer(serializers.ModelSerializer):

    worker = WorkerSerializer(many=True)
    car = CarSerializer()

    class Meta:
        model = Arrangement
        fields = "__all__"


class ArrangementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arrangement
        fields = "__all__"