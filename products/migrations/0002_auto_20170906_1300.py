# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'static/product_images/bracelet1.jpg', upload_to=b'static/product_images/'),
        ),
    ]
