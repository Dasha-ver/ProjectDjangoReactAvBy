import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from .serializers import UserSerializer, SecondPageSerializer, CarSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django_filters import FilterSet, AllValuesFilter
from django_filters import DateTimeFilter, NumberFilter
from .models import GeneralPage, SecondPage, ThirdPage, Car, Rate


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': f'Welcome to the JWT Authentication page using React Js and Django {request.user}!'}
        return Response(content)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class SecondPageView(generics.ListAPIView):
    queryset = SecondPage.objects.all()
    serializer_class = SecondPageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "count": ["gt", "exact", "range"],
    }


class CarView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "year": ["range", "gte", "lte"],
        "mark_link_text": ["in", "exact",],
        "model_link_text": ["in", "exact"],
        "card_price_primary": ["range", "gte", "lte"],
        "card_price_secondary": ["range", "gte", "lte"],
    }
