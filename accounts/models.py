# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Model to extend information for user
class UserExtras(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    house = models.CharField(max_length=25)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=8)


# Create userextras whenever a user is registered
@receiver(post_save, sender=User)
def create_userextras(sender, **kwargs):
    if kwargs['created']:
        UserExtras.objects.create(user=kwargs['instance'])


# Save userextras at the same time as user
@receiver(post_save, sender=User)
def update_userextras(sender, instance, **kwargs):
    instance.userextras.save()
