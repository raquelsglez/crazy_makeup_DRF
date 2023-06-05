# Django and DRF imports
from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins

# proof class imports
from exercises.models import Television, Nevera
from exercises.serializers import TelevisionSerializer, NeveraSerializer


class TelevisionViewSet(ModelViewSet):
    queryset = Television.objects.all()
    serializer_class = TelevisionSerializer
    lookup_field = 'numero_de_serie'


class NeveraViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Nevera.objects.all()
    serializer_class = NeveraSerializer
    lookup_field = 'id'
