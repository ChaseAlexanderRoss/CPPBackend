from django.shortcuts import render
from rest_framework import generics
from .models import Address, Item, Box, User, Order
from .serializers import AddressSerializer, BoxSerializer, ItemSerializer, UserSerializer, OrderSerializer
# Create your views here.


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class BoxList(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer


class BoxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
