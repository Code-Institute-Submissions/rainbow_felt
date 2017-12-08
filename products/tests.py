# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from .views import all_products, product_view, custom_request
from .models import Product
from .forms import CustomProductForm
import re


# Test all products page
class AllProductsPageTest(TestCase):
    def test_all_products_page(self):
        # Make sure page resolves
        allproducts_page = resolve('/products/')
        self.assertEqual(allproducts_page.func, all_products)

        # Make sure correct template used
        allproductsc = self.client.get('/products/')
        self.assertTemplateUsed(allproductsc, "products.html")

        # Make sure html is correct
        allproducts_output = render_to_response("products.html").content
        self.assertEqual(allproductsc.content, allproducts_output)


# Test product page
class ProductPageTest(TestCase):
    def test_product_page(self):
        # Create test product entry
        self.client = Client()
        self.viewed_product = Product.objects.create(id='1', name='test', description='test', price='9.99', image='static/product_images/test.jpg')

        # Make sure page resolves
        product_page = resolve('/products/1/')
        self.assertEqual(product_page.func, product_view)

        # Make sure correct template used
        productc = self.client.get('/products/1/')
        self.assertTemplateUsed(productc, "productdetails.html")

        # Make sure html is correct
        product_output = render_to_response("productdetails.html", {'viewed_product': self.viewed_product}).content
        self.assertEqual(productc.content, product_output)


# Test custom request page
class CustomRequestPageTest(TestCase):
    def test_custom_request_page(self):
        # Make sure page resolves
        customrequest_page = resolve('/customorder/')
        self.assertEqual(customrequest_page.func, custom_request)

        # Make sure correct template used
        customrequestc = self.client.get('/customorder/')
        self.assertTemplateUsed(customrequestc, "customorder.html")

        # Make sure html is correct
        customrequest_output = render_to_response("customorder.html", {'form': CustomProductForm()}).content
        # Remove csrf token
        csrf = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        new_html = re.sub(csrf, '', customrequestc.content)
        self.assertEqual(new_html, customrequest_output)


# Test custom product request form
class CustomProductFormTests(TestCase):
    def test_custom_product_form(self):
        form = CustomProductForm({
            'email': 'test@test.com',
            'custom_description': 'This is a test description',
        })
        self.assertTrue(form.is_valid())

    def test_custom_product_form_fails_with_missing_email(self):
        form = CustomProductForm({
            'custom_description': 'This is a test description',
        })
        self.assertFalse(form.is_valid())

    def test_custom_product_form_fails_with_missing_description(self):
        form = CustomProductForm({
            'email': 'test@test.com',
        })
        self.assertFalse(form.is_valid())

    def test_custom_product_form_fails_with_invalid_email(self):
        form = CustomProductForm({
            'email': 'test.com',
            'custom_description': 'This is a test description',
        })
        self.assertFalse(form.is_valid())

    def test_custom_product_form_fails_with_invalid_email_characters(self):
        form = CustomProductForm({
            'email': 'test@tes!t.com',
            'custom_description': 'This is a test description',
        })
        self.assertFalse(form.is_valid())
