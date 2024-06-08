from rest_framework import routers
from .api import GeneralPageViewSet, SecondPageViewSet, ThirdPageViewSet, CarViewSet

router = routers.DefaultRouter()
router.register('general', GeneralPageViewSet)
router.register('models', SecondPageViewSet)
router.register('marks_model', ThirdPageViewSet)
router.register('cars', CarViewSet)

urlpatterns = router.urls