from django.contrib import admin
from .models import Address, Box, Item, Product, Card, Giftcard, Order, User
# Register your models here.

admin.site.register([Address, Box, Item, Product, Card, Giftcard, Order, User])
