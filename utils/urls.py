# Django and DRF imports
from rest_framework.routers import SimpleRouter
from django.urls import path

# proof class import
from .views import MasterDataAPIView

router = SimpleRouter()

urlpatterns = [
    path('master-data', MasterDataAPIView.as_view(), name='master_data'),
]
