# Generated by Django 4.0.4 on 2022-04-22 09:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_remove_productattributevalue_product_attribute_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_creation',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 22, 9, 39, 8, 816603, tzinfo=utc), verbose_name='Date création'),
        ),
    ]
