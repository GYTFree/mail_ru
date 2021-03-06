# Generated by Django 2.1 on 2018-09-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shop', models.CharField(max_length=48, unique=True)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('client_id', models.CharField(max_length=128)),
                ('client_secret', models.CharField(max_length=128)),
                ('grant_type', models.CharField(default='password', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('product_id', models.CharField(max_length=64, null=True)),
                ('sku', models.CharField(max_length=64)),
                ('color', models.CharField(max_length=64, null=True)),
                ('color_name', models.CharField(max_length=64, null=True)),
                ('size', models.CharField(max_length=64, null=True)),
                ('inventory', models.FloatField()),
                ('price', models.FloatField()),
                ('shipping', models.IntegerField()),
                ('msrp', models.FloatField()),
                ('enabled', models.BooleanField()),
                ('shipping_time', models.CharField(max_length=48)),
                ('main_image', models.CharField(max_length=255)),
                ('updated_at', models.CharField(max_length=48)),
                ('all_images', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spu',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('shop', models.CharField(default=None, max_length=48)),
                ('name', models.CharField(max_length=255)),
                ('parent_sku', models.CharField(default=None, max_length=255)),
                ('num_sold', models.CharField(max_length=48, null=True)),
                ('num_saves', models.CharField(max_length=48, null=True)),
                ('review_status', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=48, null=True)),
                ('upc', models.IntegerField(null=True)),
                ('landing_page_url', models.CharField(max_length=255, null=True)),
                ('main_image', models.CharField(max_length=255)),
                ('enabled', models.CharField(max_length=32)),
                ('is_promoted', models.CharField(max_length=32)),
                ('original_image_url', models.CharField(max_length=255)),
                ('date_uploaded', models.CharField(max_length=48)),
                ('last_updated', models.CharField(max_length=48)),
                ('wish_express_country_codes', models.CharField(max_length=255, null=True)),
                ('shipping_category', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
