# Django and DRF imports
from rest_framework.routers import SimpleRouter

# proof class import
from .views import TelevisionViewSet, NeveraViewSet

router = SimpleRouter()

router.register(r'television', TelevisionViewSet, basename="television"),
router.register(r'nevera', NeveraViewSet, basename="nevera")

urlpatterns = router.urls
