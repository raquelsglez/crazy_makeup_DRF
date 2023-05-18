# Django and DRF imports
from rest_framework.viewsets import ModelViewSet

# proof class imports
from .serializers import MakeupProductSerializer, UpdateMakeupProductSerializer
from makeup_product.models import MakeupProduct


class MakeupProductViewSet(ModelViewSet):
    queryset = MakeupProduct.objects.all()  # de donde vienen nuestros datos
    serializer_class = MakeupProductSerializer
    lookup_field = "id"  # Para buscar el producto por su id

    def get_serializer_class(self):
        if self.action in ["partial_update", "update"]:
            return UpdateMakeupProductSerializer
        return self.serializer_class
