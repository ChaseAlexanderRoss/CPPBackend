from rest_framework import serializers
from .models import Address, Box, Item, Order, User


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    addresses = serializers.HyperlinkedRelatedField(
        view_name='addresses_detail',
        read_only=True
    )

    class Meta:
        model = Address
        fields = ('id', 'name', 'street_1', 'street_2', 'city',
                  'zip_code', 'state', 'country', 'addresses')


class BoxSerializer(serializers.HyperlinkedModelSerializer):
    boxes = serializers.HyperlinkedRelatedField(
        view_name='boxes_detail',
        read_only=True
    )

    class Meta:
        model = Box
        fields = ('design', 'title', 'total_cost', 'shipping_address', 'boxes')


class ItemSerializer:
    items = serializers.HyperlinkedRelatedField(
        view_name='items_detail',
        read_only=True
    )

    class Meta:
        model = Item
        fields = ('name', 'picture', 'price',
                  'occasion', 'product_type', 'items')


class UserSerializer:
    users = serializers.HyperlinkedRelatedField(
        view_name='users_detail',
        read_only=True
    )

    class Meta:
        model = User
        fields = ('name', 'credit_card_num', 'credit_card_sec_code',
                  'credit_card_exp_date', 'users')


class OrderSerializer:
    orders = serializers.HyperlinkedRelatedField(
        view_name='orders_detail',
        read_only=True
    )

    class Meta:
        model = Item
        fields = ('name', 'picture', 'price',
                  'occasion', 'product_type', 'items')
