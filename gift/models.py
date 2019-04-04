from django.db import models

# Create your models here.


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
    item_type = models.CharField(max_length=100)


class Product(models.Model):
    item_id = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='product_item_id')
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    price = models.IntegerField()
    occasion = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)


class Card(models.Model):
    item_id = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='card_item_id')
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    price = models.IntegerField()
    occasion = models.CharField(max_length=100)
    message = models.CharField(max_length=200)


class Giftcard(models.Model):
    item_id = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='giftcard_item_id')
    store = models.CharField(max_length=100)
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
