from django.shortcuts import render
from rest_framework import generics
from .models import Address, Item, Product, Box
from .serializers import AddressSerializer
# Create your views here.

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    