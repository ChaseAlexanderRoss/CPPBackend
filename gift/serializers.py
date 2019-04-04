from rest_framework import serializers
from .models import Address, Box, Item, Product, Card, Giftcard, Order, User

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    addresses = serializers.HyperlinkedRelatedField(
    view_name='address_detail',
    read_only=True
    )

    class Meta:
        model = Address
        fields = ('id', 'name', 'street_1', 'street_2', 'city', 'zip_code', 'state', 'country', 'addresses')

class BoxSerializer(serializers.HyperlinkedModelSerializer):
    boxes = serializers.HyperlinkedRelatedField(
    view_name='box_detail',
    )

    class Meta:
        model = Box
        fields = ('design','title','total_cost','shipping_address', 'boxes')

# class ItemSerializer(serializers.HyperlinkedModelSerializer):
#     items = serializers.HyperlinkedRelatedField(
#     view_name='item_view'
#     )

#     class Meta:
#         model = Item
#         fields = ('item_type')


# class ProductSerializer(serializers.HyperlinkedModelSerializer):
#     products = serializers.HyperlinkedRelatedField(
#     view_name='product_view'
#     )

#     class Meta:
#         model = Product
#         fields = ('item_id','name','picture','price','occasion','product_type')