from .models import GeneralPage, SecondPage, ThirdPage, Car, Rate
from rest_framework import viewsets, permissions
from .serializers import GeneralPageSerializer, SecondPageSerializer, ThirdPageSerializer, CarSerializer, RateSerializer
from django.db.models import Q


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


class SecondPageViewSet(viewsets.ModelViewSet):
    queryset = SecondPage.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SecondPageSerializer


class ThirdPageViewSet(viewsets.ModelViewSet):
    queryset = ThirdPage.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ThirdPageSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer


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


class YearFromViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

    def get_queryset(self):
        if (year := self.kwargs.get("year", None)) is not None:
            return Car.objects.filter(year__gte=year)

        return super().get_queryset()


class YearToViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

    def get_queryset(self):
        if (year := self.kwargs.get("year", None)) is not None:
            return Car.objects.filter(year__lte=year)

        return super().get_queryset()


class YearsRangeViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

    def get_queryset(self):
        if (yearFrom := self.kwargs.get("year", None)) is not None:
            return Car.objects.filter(year__range=(yearFrom, 2022))

        return super().get_queryset()
