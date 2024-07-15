from .models import GeneralPage, SecondPage, ThirdPage, Car, Rate
from rest_framework import viewsets, permissions, generics
from .serializers import GeneralPageSerializer, SecondPageSerializer, ThirdPageSerializer, CarSerializer, RateSerializer
from django_filters import FilterSet, AllValuesFilter
from django_filters import DateTimeFilter, NumberFilter


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RateSerializer


class GeneralPageViewSet(viewsets.ModelViewSet):
    queryset = GeneralPage.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GeneralPageSerializer


class ThirdPageViewSet(viewsets.ModelViewSet):
    queryset = ThirdPage.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ThirdPageSerializer


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

    def get_queryset(self):
        if (mark_link_text := self.kwargs.get("mark_link_text", None)) is not None:
            return Car.objects.filter(mark_link_text__icontains=mark_link_text)
        return super().get_queryset()


class MarkModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

    def get_queryset(self):
        if (model_link_text := self.kwargs.get("model_link_text", None)) is not None:
            return Car.objects.filter(model_link_text__icontains=model_link_text)

        return super().get_queryset()


