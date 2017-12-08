# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from .views import index_page, about_page


# Test homepage
class HomePageTest(TestCase):
    def test_home_page(self):
        home = resolve('/')
        self.assertEqual(home.func, index_page)
        homec = self.client.get('/')
        self.assertTemplateUsed(homec, "index.html")
        home_output = render_to_response("index.html").content
        self.assertEqual(homec.content, home_output)


# Test about page
class AboutPageTest(TestCase):
    def test_about_page(self):
        about = resolve('/about/')
        self.assertEqual(about.func, about_page)
        aboutc = self.client.get('/about/')
        self.assertTemplateUsed(aboutc, "about.html")
        about_output = render_to_response("about.html").content
        self.assertEqual(aboutc.content, about_output)
