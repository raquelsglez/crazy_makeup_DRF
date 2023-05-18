# Django and DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response

# proof class import
from makeup_product.models import ColorType


class MasterDataAPIView(APIView):
    def get(self, request):
        color_choices = ColorType.get_all_choices()

        return Response(
            {
                'color_choices': color_choices,
            },

        )