# Django and DRF imports
import django_filters
from rest_framework import status, mixins
from rest_framework.decorators import action
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

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("me_list", "me"):
            queryset = queryset.filter(user=self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['PUT', 'PATCH', 'DELETE'])
    def me(self, request, id):

        if request.method in ('PUT', 'PATCH'):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        elif request.method == 'DELETE':
            instance = self.get_object()
            instance.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'], url_path="me-list", url_name="me-list")
    def me_list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "create":
            return CreateMakeupProductSerializer
        elif self.action == 'me':
            return UpdateMakeupProductSerializer
        elif self.action == 'me_list':
            return ListProfileMakeupProductSerializer

        return self.serializer_class
