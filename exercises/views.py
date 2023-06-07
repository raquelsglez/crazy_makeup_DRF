# Django and DRF imports
import django_filters
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

# proof class imports
from exercises.models import Television, Nevera
from exercises.serializers import TelevisionSerializer, NeveraSerializer


class TelevisionViewSet(ModelViewSet):
    queryset = Television.objects.all()
    serializer_class = TelevisionSerializer
    lookup_field = 'numero_de_serie'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]

    filterset_fields = {
        "pulgadas": ["lt", "lte", "exact", "gte", "gt", "in"],
        "numero_de_serie": ["in", "icontains", "exact"]
    }

    search_fields = ['pulgadas']
    ordering_fields = "__all__"


class NeveraViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Nevera.objects.all()
    serializer_class = NeveraSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]

    filterset_fields = {
        "marca": ["icontains", "isnull", "exact", "in"],
        "altura": ["lt", "lte", "exact", "gte", "gt", "in"],
        "nombre": ["icontains"],
        "color": ["icontains", "exact", "in"],
        "anchura": ["lt", "lte", "exact", "gte", "gt", "in"]
    }

    search_fields = ['color', 'nombre', 'marca']
    ordering_fields = "__all__"
