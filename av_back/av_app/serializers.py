from rest_framework import serializers
from .models import GeneralPage, SecondPage, ThirdPage, Car, User, Rate, UserCarRelation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


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


class UserCarRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCarRelation
        fields = '__all__'
