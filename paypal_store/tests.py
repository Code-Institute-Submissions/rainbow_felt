# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from .views import paypal_cancel, paypal_return


# Test my paypal return page resolves correctly
class PaypalReturnPageTest(TestCase):
    def test_paypal_return_page(self):
        # Create temp user and login as @login-required
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'testtest')
        self.client.login(username='test', password='testtest')
        # Make sure page resolves
        paypal_return_page = resolve('/paypal-return/')
        self.assertEqual(paypal_return_page.func, paypal_return)


# Test my paypal cancel page resolves correctly
class PaypalCancelPageTest(TestCase):
    def test_paypal_cancel_page(self):
        # Create temp user and login as @login-required
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'testtest')
        self.client.login(username='test', password='testtest')
        # Make sure page resolves
        paypal_cancel_page = resolve('/paypal-cancel/')
        self.assertEqual(paypal_cancel_page.func, paypal_cancel)
