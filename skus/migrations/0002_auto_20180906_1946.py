# Generated by Django 2.1 on 2018-09-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spu',
            name='parent_sku',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
