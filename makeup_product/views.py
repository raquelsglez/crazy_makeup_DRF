# Django and DRF imports
import django_filters
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import GenericViewSet

# proof class imports
from .serializers import (ListMakeupProductSerializer,
                          UpdateMakeupProductSerializer,
                          CreateMakeupProductSerializer,
                          ListProfileMakeupProductSerializer)
from makeup_product.models import MakeupProduct


class MakeupProductViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    queryset = MakeupProduct.objects.all()  # de donde vienen nuestros datos
    serializer_class = ListMakeupProductSerializer
    lookup_field = "id"  # Para buscar el producto por su id
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]

    filterset_fields = {
        "stock": ["lt", "lte", "exact", "gte", "gt", "in"],
        "name": ["icontains", "exact"],
        "trademark": ["icontains", "isnull", "exact", "in"],
        "color": ["icontains", "exact", "in"],
        "price": ["lt", "lte", "exact", "gte", "gt", "in"]
    }

    search_fields = ['name', 'color', 'trademark']
    ordering_fields = ['name', 'color', 'trademark', 'price']

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action == "create":
            return CreateMakeupProductSerializer
        return self.serializer_class


class MeMakeupProductView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):

    queryset = MakeupProduct.objects.all()
    serializer_class = ListProfileMakeupProductSerializer
    lookup_field = "id"

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.action in ("update", "partial_update"):
            return UpdateMakeupProductSerializer
        return self.serializer_class