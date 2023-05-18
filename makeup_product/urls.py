# Django and DRF imports
from rest_framework.routers import SimpleRouter

# proof class import
from .views import MakeupProductViewSet

router = SimpleRouter()  # crea rutas

router.register(r'makeup-products', MakeupProductViewSet, basename="makeup_products")

urlpatterns = router.urls