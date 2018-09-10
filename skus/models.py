from django.db import models


# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    shop = models.CharField(max_length=48, unique=True, null=False)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32, null=False)
    client_id = models.CharField(max_length=128)
    client_secret = models.CharField(max_length=128)
    grant_type = models.CharField(max_length=64, default='password')

    def __str__(self):
        return self.shop


class Spu(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    shop = models.CharField(max_length=48, default=None)
    name = models.CharField(max_length=255)
    parent_sku = models.CharField(max_length=255, default=None, null=True)
    num_sold = models.CharField(max_length=48, null=True)
    num_saves = models.CharField(max_length=48, null=True)
    review_status = models.CharField(max_length=64)
    description = models.TextField()
    brand = models.CharField(max_length=48, null=True)
    upc = models.IntegerField(null=True)
    landing_page_url = models.CharField(max_length=255, null=True)
    main_image = models.CharField(max_length=255)
    enabled = models.CharField(max_length=32)
    is_promoted = models.CharField(max_length=32)
    original_image_url = models.CharField(max_length=255)
    date_uploaded = models.CharField(max_length=48)
    last_updated = models.CharField(max_length=48)
    wish_express_country_codes = models.CharField(max_length=255, null=True)
    shipping_category = models.CharField(max_length=255, null=True)


class Sku(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    product_id = models.CharField(max_length=64, null=True)
    sku = models.CharField(max_length=64)
    color = models.CharField(max_length=64, null=True)
    color_name = models.CharField(max_length=64, null=True)
    size = models.CharField(max_length=64, null=True)
    inventory = models.FloatField()
    price = models.FloatField()
    shipping = models.IntegerField()
    msrp = models.FloatField()
    enabled = models.BooleanField()
    shipping_time = models.CharField(max_length=48)
    main_image = models.CharField(max_length=255)
    updated_at = models.CharField(max_length=48)
    all_images = models.TextField(null=True)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=64)
    product_id = models.CharField(max_length=64)
    transaction_id = models.CharField(max_length=64)
    variant_id = models.CharField(max_length=64)
    buyer_id = models.CharField(max_length=64)
    quantity = models.IntegerField()
    sku = models.CharField(max_length=128)
    size = models.CharField(max_length=16)
    color = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    shipping_provider = models.CharField(max_length=32)
    tracking_number = models.CharField(max_length=64, null=True)
    shipped_date = models.CharField(max_length=64, null=True)
    ship_note = models.CharField(max_length=64, null=True)
    last_updated = models.CharField(max_length=64)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    days_to_fulfill = models.IntegerField()
    hours_to_fulfill = models.IntegerField()
    expected_ship_date = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.IntegerField()
    shipping_cost = models.IntegerField()
    product_name = models.TextField()
    product_image_url = models.TextField()
    order_time = models.CharField(max_length=64)
    refunded_by = models.CharField(max_length=64, null=True)
    refunded_time = models.CharField(max_length=64, null=True)
    refunded_reason = models.CharField(max_length=255, null=True)
    is_wish_express = models.CharField(max_length=16, null=True)
    we_required_delivery_date = models.CharField(max_length=64, null=True)
    tracking_confirmed = models.CharField(max_length=16, null=True)
    tracking_confirmed_date = models.CharField(max_length=64, null=True)
    requires_delivery_confirmation = models.CharField(max_length=16, null=True)
    shop_name = models.CharField(max_length=32)


class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    buyer_id = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=32)
    state = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=64)
    street_address1 = models.CharField(max_length=255)
    street_address2 = models.CharField(max_length=255, null=True)
