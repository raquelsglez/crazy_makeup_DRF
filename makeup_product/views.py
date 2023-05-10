# Django and DRF import
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# proof class imports
from makeup_product.models import MakeupProduct
from makeup_product.serializers import MakeupProductSerializer


class MakeupProductViewSet(GenericViewSet):

    queryset = MakeupProduct.objects.all()  # de donde vienen nuestros datos
    serializer_class = MakeupProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
