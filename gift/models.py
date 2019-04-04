from django.db import models

# Create your models here.

BOX_DESIGNS = (
    ('Cozy', 'COZY'),
    ('Congratulations', 'CONGRATULATIONS'),
    ('Natural', 'NATURAL')
)

ITEM_TYPES = (
    ('product', 'PRODUCT'),
    ('card', 'CARD'),
    ('gift card', 'GIFTCARD')
)

OCCASIONS = (
    ('All occasions', 'ALLOCCASIONS'),
    ('Birthday', 'BIRTHDAY'),
    ('Cheer Up', 'CHEERUP'),
    ('Congratulations', 'CONGRATULATIONS'),
    ('New Baby', 'NEWBABY'),
    ('Housewarming', 'HOUSEWARMING'),
    ('Breakup', 'BREAKUP'),
    ('Engagement', 'ENGAGEMENT'),
    ('Holiday', 'HOLIDAY'),
    ('New Job', 'NEWJOB'),
    ('Galentine\'s Day', 'GALENTINESDAY'),
    ('For Mom', 'FORMOM'),
    ('For Dad', 'FORDAD'),
    ('Lux Box', 'LUXBOX')
)

PRODUCT_TYPES = (
    ('All Types', 'ALLTYPES'),
    ('Party Supply', 'PARTY SUPPLY'),
    ('Accessories', 'ACCESSORIES'),
    ('Jewelry', 'JEWELRY'),
    ('Houseware', 'HOUSEWARE'),
    ('Spa', 'SPA'),
    ('Candles', 'CANDLES'),
    ('Stationary', 'STATIONARY')
)

GIFTCARD_STORES = (
    ('Postmates', 'POSTMATES'),
    ('Starbucks', 'STARBUCKS'),
    ('Airline', 'AIRLINE'),
    ('Nordstrom', 'NORDSTROM')
)


class Address(models.Model):
    name = models.CharField(max_length=100)
    street_1 = models.CharField(max_length=100)
    street_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=100)


class Box(models.Model):
    design = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    total_cost = models.IntegerField()
    shipping_address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name='shipping_address')


class Item(models.Model):
    item_type = models.CharField(
        max_length=100, choices=ITEM_TYPES, default='product')


class Product(models.Model):
    item_id = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='product_item_id')
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    price = models.IntegerField()
    occasion = models.CharField(
        max_length=100, choices=OCCASIONS, default='All Occasions')
    product_type = models.CharField(
        max_length=100, choices=PRODUCT_TYPES, default='All Types')


class Card(models.Model):
    item_id = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='card_item_id')
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    price = models.IntegerField()
    occasion = models.CharField(
        max_length=100, choices=OCCASIONS, default='All Occasions')
    message = models.CharField(max_length=200)


class Giftcard(models.Model):
    item_id = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='giftcard_item_id')
    store = models.CharField(
        max_length=100, choices=GIFTCARD_STORES, default='Postmates')
    amount = models.IntegerField()


class Order(models.Model):
    box_id = models.ForeignKey(
        Box, on_delete=models.CASCADE, related_name='order_box_id')
    item_id = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='order_item_id')
    quantity = models.IntegerField()


class User(models.Model):
    # add username and password if we get to authentication
    name = models.CharField(max_length=100)
    credit_card_num = models.IntegerField()
    credit_card_sec_code = models.IntegerField()
    credit_card_exp_date = models.CharField(max_length=5)
