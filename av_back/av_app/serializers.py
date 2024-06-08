from rest_framework import serializers
from .models import GeneralPage, SecondPage, ThirdPage, Car


class GeneralPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralPage
        fields = '__all__'


class SecondPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondPage
        fields = '__all__'


class ThirdPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdPage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
