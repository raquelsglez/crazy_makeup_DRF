# Django and DRF imports
import django_filters
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, GenericViewSet

# proof class imports
from activities.permissions import IsUserDni, IsUserIsStaff, IsUserPhone
from activities.models import CarWorkshop, Worker, Car, Arrangement
from activities.serializers import (CarWorkshopSerializer,
                                    WorkerSerializer,
                                    CarSerializer,
                                    ArrangementSerializer, ListArrangementSerializer, RetrieveWorkerSerializer,
                                    RetrieveCarWorkshopSerializer
                                    )


class CarWorkshopViewSet(ModelViewSet):
    queryset = CarWorkshop.objects.all()
    serializer_class = CarWorkshopSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsUserDni, IsUserIsStaff]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]

    filterset_fields = {
        "name": ["icontains", "exact", "in"],
        "address": ["icontains", "exact", "in"],
        "cif": ["icontains", "exact", "in"]
    }

    search_fields = ['name', 'address']
    ordering_fields = "__all__"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RetrieveCarWorkshopSerializer
        return self.serializer_class


class WorkerViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    GenericViewSet
                    ):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    lookup_field = 'name'

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsUserIsStaff]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]

    filterset_fields = {
        "name": ["icontains", "exact", "in"],
        "phone_number": ["icontains", "isnull", "exact", "in"],
        "dni": ["icontains", "exact", "in"],
        "car_workshop": ["exact", "in"]
    }

    search_fields = ['name', 'dni']
    ordering_fields = "__all__"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RetrieveWorkerSerializer
        return self.serializer_class


class CarViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 GenericViewSet
                 ):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'car_license_plate'

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsUserDni]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]

    filterset_fields = {
        "car_license_plate": ["icontains", "exact", "in"],
        "trademark": ["icontains", "exact", "in"],
        "model": ["icontains", "exact", "in"],
        "color": ["icontains", "isnull", "exact", "in"]
    }

    search_fields = ['model', 'trademark']
    ordering_fields = "__all__"


class ArrangementViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         GenericViewSet
                         ):
    queryset = Arrangement.objects.all()
    serializer_class = ArrangementSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsUserDni, IsUserPhone]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]

    filterset_fields = {
        "date_time": ["lt", "lte", "exact", "gte", "gt", "in"],
        "worker": ["icontains", "exact", "in"],
        "car": ["icontains", "exact", "in"],

    }

    search_fields = ['datetime']
    ordering_fields = "__all__"
    
    def get_serializer_class(self):
        if self.action == "list":
            return ListArrangementSerializer
        return self.serializer_class
