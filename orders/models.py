# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Model for customer orders
class Order(models.Model):
    # Protect to prevent users with orders being deleted
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='orders')
    invoice = models.UUIDField(editable=False)
    items = models.IntegerField()
    quantities = models.IntegerField()
