from rest_framework import routers
from django.urls import path
from .api import GeneralPageViewSet, SecondPageViewSet, ThirdPageViewSet, CarViewSet, RateViewSet
from .views import *
from . import views

router = routers.DefaultRouter()
router.register('general', GeneralPageViewSet)
router.register('models', SecondPageViewSet)
router.register('marks_model', ThirdPageViewSet)
router.register('cars', CarViewSet)
router.register('rate', RateViewSet)

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view()),
]
urlpatterns += router.urls
