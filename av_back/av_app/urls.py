from django.urls import path
from rest_framework import routers
from .api import GeneralPageViewSet, ThirdPageViewSet, RateViewSet
from .views import *

router = routers.DefaultRouter()
router.register('general', GeneralPageViewSet)
router.register('marks_model', ThirdPageViewSet)
router.register('rate', RateViewSet)

urlpatterns = [
    path('cars/', CarView.as_view(), name='cars'),
    path('models/', SecondPageView.as_view(), name='models'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view()),
]
urlpatterns += router.urls
