# Generated by Django 2.1 on 2018-09-10 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skus', '0002_auto_20180906_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('buyer_id', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('zipcode', models.CharField(max_length=64)),
                ('street_address1', models.CharField(max_length=64)),
                ('street_address2', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=64)),
                ('product_id', models.CharField(max_length=64)),
                ('transaction_id', models.CharField(max_length=64)),
                ('variant_id', models.CharField(max_length=64)),
                ('buyer_id', models.CharField(max_length=64)),
                ('quantity', models.IntegerField()),
                ('sku', models.CharField(max_length=128)),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=32)),
                ('shipping_provider', models.CharField(max_length=32)),
                ('tracking_number', models.CharField(max_length=64, null=True)),
                ('shipped_date', models.CharField(max_length=64, null=True)),
                ('ship_note', models.CharField(max_length=64, null=True)),
                ('last_updated', models.CharField(max_length=64)),
                ('order_total', models.IntegerField()),
                ('days_to_fulfill', models.IntegerField()),
                ('hours_to_fulfill', models.IntegerField()),
                ('expected_ship_date', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping', models.IntegerField()),
                ('shipping_cost', models.IntegerField()),
                ('product_name', models.TextField()),
                ('product_image_url', models.TextField()),
                ('order_time', models.CharField(max_length=64)),
                ('refunded_by', models.CharField(max_length=64, null=True)),
                ('refunded_time', models.CharField(max_length=64, null=True)),
                ('refunded_reason', models.CharField(max_length=255, null=True)),
                ('is_wish_express', models.CharField(max_length=16, null=True)),
                ('we_required_delivery_date', models.CharField(max_length=64, null=True)),
                ('tracking_confirmed', models.CharField(max_length=16, null=True)),
                ('tracking_confirmed_date', models.CharField(max_length=64, null=True)),
                ('requires_delivery_confirmation', models.CharField(max_length=16, null=True)),
                ('shop_name', models.CharField(max_length=32)),
            ],
        ),
    ]
