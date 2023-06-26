# Django and DRF imports
import django_filters

from rest_framework import mixins, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

# proof class imports
from exercises2.models import Building, Flat
from exercises2.serializers import (
    ListBuildingSerializer,
    FlatSerializer,
    UpdateFlatSerializer,
    CreateBuildingSerializer,
    UpdateBuildingSerializer
)


class BuildingViewSet(ModelViewSet):

    queryset = Building.objects.all()
    serializer_class = ListBuildingSerializer
    lookup_field = 'id'

    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]

    filterset_fields = {
        "n_floors": ["lt", "lte", "exact", "gte", "gt", "in"],
        "number": ["icontains", "exact", "in"],
        "total_flats": ["lt", "lte", "exact", "gte", "gt", "in"]
    }

    search_fields = ['street']
    ordering_fields = "__all__"

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return CreateBuildingSerializer
        elif self.action in ("update", "partial_update"):
            return UpdateBuildingSerializer
        return self.serializer_class


class FlatViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):

    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'

    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]

    filterset_fields = {
        "square_meter": ["lt", "lte", "exact", "gte", "gt", "in"],
        "n_rooms": ["lt", "lte", "exact", "gte", "gt", "in"],
        "n_bathrooms": ["lt", "lte", "exact", "gte", "gt", "in"],
        "floor": ["lt", "lte", "exact", "gte", "gt", "in"],
        "letter": ["icontains", "exact", "in"],
        "user": ["exact", "in"],
        "building": ["exact", "in"],
        "building__street": ["icontains", "exact", "in"]
    }

    search_fields = ['user__first_name']
    ordering_fields = "__all__"

    def get_permissions(self):
        if self.action in ['create']:
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


class MeFlatView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Flat.objects.all()
    serializer_class = UpdateFlatSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
