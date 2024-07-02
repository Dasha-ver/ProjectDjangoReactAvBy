from django.urls import path
from rest_framework import routers
from .api import GeneralPageViewSet, SecondPageViewSet, ThirdPageViewSet, CarViewSet, RateViewSet, MarkModelViewSet, \
    MarkViewSet, YearFromViewSet, YearToViewSet, YearsRangeViewSet
from .views import *

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
    path("carmark/<str:mark_link_text>/", MarkViewSet.as_view(actions={"get": "list"}),
         name="mark-by-mark_link_text", ),
    path("carmodel/<str:model_link_text>/", MarkModelViewSet.as_view(actions={"get": "list"}), name="model-by"
                                                                                                    "-model_link_text",
         ),
    path("carsyearfrom/<str:year>/", YearFromViewSet.as_view(actions={"get": "list"}), name="year-by"
                                                                                            "-year_from_link_text", ),
    path("carsyearto/<str:year>/", YearToViewSet.as_view(actions={"get": "list"}), name="year-by"
                                                                                        "-year_to_link_text", ),
    path("carsyearsrange/<str:year>/", YearsRangeViewSet.as_view(actions={"get": "list"}), name="year-by"
                                                                                                "-years_range_link_text", ),
]
urlpatterns += router.urls
