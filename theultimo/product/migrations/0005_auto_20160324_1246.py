# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-24 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imageLink',
            field=models.FileField(upload_to=b''),
        ),
    ]
