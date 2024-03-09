from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import Orders, Services


# пользователи
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


# заявки
class OrdersList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = serializers.OrderSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = serializers.OrderSerializer

# Сервисы

class ServicesList(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = serializers.ServiceSerializer
