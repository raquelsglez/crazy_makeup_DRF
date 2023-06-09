# Django and DRF imports
import django_filters
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
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

    def get_permissions(self):
        if self.action in ('create', 'favorite', 'unfavorite'):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

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

    @action(detail=True, methods=['POST'])
    def favorite(self, request, id):
        makeup_product = self.get_object()
        self.request.user.do_favorite(makeup_product)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['POST'])
    def unfavorite(self, request, id):
        makeup_product = self.get_object()
        self.request.user.do_unfavorite(makeup_product)
        return Response(status=status.HTTP_204_NO_CONTENT)


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