# Django and DRF imports
from rest_framework.routers import SimpleRouter

# proof class import
from .views import BuildingViewSet, FlatViewSet, MeFlatView

router = SimpleRouter()

router.register(r'buildings', BuildingViewSet, basename="buildings"),
router.register(r'flats', FlatViewSet, basename="flats")
router.register(r'me/flats', MeFlatView, basename="me_flats")

urlpatterns = router.urls
