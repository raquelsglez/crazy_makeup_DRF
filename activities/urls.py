# Django and DRF imports
from rest_framework.routers import SimpleRouter

# proof class import
from .views import CarWorkshopViewSet, CarViewSet, WorkerViewSet, ArrangementViewSet

router = SimpleRouter()

router.register(r'car-work-shop', CarWorkshopViewSet, basename="car_work_shop"),
router.register(r'car', CarViewSet, basename="car"),
router.register(r'worker', WorkerViewSet, basename="worker"),
router.register(r'arrangement', ArrangementViewSet, basename="arrangement")

urlpatterns = router.urls