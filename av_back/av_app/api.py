from .models import GeneralPage, SecondPage, ThirdPage, Car, Rate
from rest_framework import viewsets, permissions
from .serializers import GeneralPageSerializer, SecondPageSerializer, ThirdPageSerializer, CarSerializer, RateSerializer


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
