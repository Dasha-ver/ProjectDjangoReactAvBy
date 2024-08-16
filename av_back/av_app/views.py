from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import UpdateModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .serializers import UserSerializer, SecondPageSerializer, CarSerializer, UserCarRelationSerializer
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import SecondPage, Car, UserCarRelation


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'username': f'{request.user}',
                   'userId': f'{request.user.id}'}
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


class SecondPageView(viewsets.ModelViewSet):
    queryset = SecondPage.objects.all()
    serializer_class = SecondPageSerializer


class CarView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "id": ["in", "exact"],
        "year": ["range", "gte", "lte"],
        "mark_link_text": ["in", "exact", ],
        "model_link_text": ["in", "exact"],
        "card_price_primary": ["range", "gte", "lte"],
        "card_price_secondary": ["range", "gte", "lte"],
    }


class UserCarRelationView(generics.ListAPIView):
    queryset = UserCarRelation.objects.all()
    serializer_class = UserCarRelationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "user": ["in", "exact", ],
        "car": ["in", "exact", ],
    }

    def post(self, request):
        serializer = UserCarRelationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteObject(APIView):
    def delete(self, request, pk):
        try:
            obj = UserCarRelation.objects.get(pk=pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserCarRelation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
