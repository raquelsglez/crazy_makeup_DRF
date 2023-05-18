# Django and DRF imports
from rest_framework.viewsets import ModelViewSet

# proof class imports
from .serializers import ListMakeupProductSerializer, UpdateMakeupProductSerializer, CreateMakeupProductSerializer
from makeup_product.models import MakeupProduct


class MakeupProductViewSet(ModelViewSet):
    queryset = MakeupProduct.objects.all()  # de donde vienen nuestros datos
    serializer_class = ListMakeupProductSerializer
    lookup_field = "id"  # Para buscar el producto por su id

    def get_serializer_class(self):
        if self.action in ["partial_update", "update"]:
            return UpdateMakeupProductSerializer
        elif self.action == "create":
            return CreateMakeupProductSerializer
        return self.serializer_class
