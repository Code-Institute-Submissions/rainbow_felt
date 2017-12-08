# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test.client import Client
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from .views import login, logout, register, myaccount
from .forms import UserLoginForm, UserRegistrationForm, ExtrasForm
import re


# Test views work correctly
class AccountPagesTest(TestCase):
    def test_login_page(self):
        # Make sure page resolves
        login_page = resolve('/login/')
        self.assertEqual(login_page.func, login)

        # Make sure correct template used
        loginc = self.client.get('/login/')
        self.assertTemplateUsed(loginc, "login.html")

        # Make sure html is correct
        login_output = render_to_response("login.html", {'form': UserLoginForm()}).content
        # Remove csrf token
        csrf = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        new_html = re.sub(csrf, '', loginc.content)
        self.assertEqual(new_html, login_output)

    def test_logout_page(self):
        # Make sure page resolves
        logout_page = resolve('/logout/')
        self.assertEqual(logout_page.func, logout)

        # Make sure redirected to home template
        logoutc = self.client.get('/logout/')
        self.assertTemplateUsed(logoutc, "index.html")

    def test_register_page(self):
        # Make sure page resolves
        register_page = resolve('/register/')
        self.assertEqual(register_page.func, register)

        # Make sure correct template used
        registerc = self.client.get('/register/')
        self.assertTemplateUsed(registerc, "register.html")

        # Make sure html is correct
        register_output = render_to_response("register.html", {'form': UserRegistrationForm()}).content
        # Remove csrf token
        csrf = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        new_html = re.sub(csrf, '', registerc.content)
        self.assertEqual(new_html, register_output)

    def test_myaccount_page(self):
        # Create temp user and login as @login-required
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'testtest')
        self.client.login(username='test', password='testtest')

        # Make sure page resolves
        myaccount_page = resolve('/myaccount/')
        self.assertEqual(myaccount_page.func, myaccount)

        # Make sure correct template used
        myaccountc = self.client.get('/myaccount/')
        self.assertTemplateUsed(myaccountc, "myaccount.html")

        # Make sure html is correct
        myaccount_output = render_to_response("myaccount.html", {'form': ExtrasForm(), 'user': self.user}).content
        # Remove csrf token
        csrf = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        new_html = re.sub(csrf, '', myaccountc.content)
        self.assertEqual(new_html, myaccount_output)


class RegistrationFormTests(TestCase):
    def test_registration_form(self):
        form = UserRegistrationForm({
            'username': 'test',
            'email': 'test@test.com',
            'password1': 'testblob',
            'password2': 'testblob',
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_username(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'testblob',
            'password2': 'testblob',
        })
        self.assertFalse(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'username': 'test',
            'password1': 'testblob',
            'password2': 'testblob',
        })
        self.assertFalse(form.is_valid())

    def test_registration_form_fails_with_missing_password1(self):
        form = UserRegistrationForm({
            'username': 'test',
            'email': 'test@test.com',
            'password2': 'testblob',
        })
        self.assertFalse(form.is_valid())

    def test_registration_form_fails_with_missing_password2(self):
        form = UserRegistrationForm({
            'username': 'test',
            'email': 'test@test.com',
            'password1': 'testblob',
        })
        self.assertFalse(form.is_valid())

    def test_registration_form_fails_without_matching_passwords(self):
        form = UserRegistrationForm({
            'username': 'test',
            'email': 'test@test.com',
            'password1': 'testtbloob',
            'password2': 'testblob',
        })
        self.assertFalse(form.is_valid())

    def test_registration_form_fails_with_too_simple_password(self):
        form = UserRegistrationForm({
            'username': 'test',
            'email': 'test@test.com',
            'password1': 'testtest',
            'password2': 'testtest',
        })
        self.assertFalse(form.is_valid())

    def test_registration_form_fails_with_invalid_email(self):
        form = UserRegistrationForm({
            'username': 'test',
            'email': 'testst.com',
            'password1': 'testblob',
            'password2': 'testblob',
        })
        self.assertFalse(form.is_valid())

    def test_registration_form_fails_with_invalid_characters(self):
        form = UserRegistrationForm({
            'username': 'test!',
            'email': 'test@test.com',
            'password1': 'testblob',
            'password2': 'testblob',
        })
        self.assertFalse(form.is_valid())


class LoginFormTests(TestCase):
    def test_login_form(self):
        form = UserLoginForm({
            'username': 'test',
            'password': 'testblob',
        })
        self.assertTrue(form.is_valid())

    def test_login_form_fails_with_missing_username(self):
        form = UserLoginForm({
            'password': 'testblob',
        })
        self.assertFalse(form.is_valid())

    def test_login_form_fails_with_missing_password(self):
        form = UserLoginForm({
            'username': 'test',
        })
        self.assertFalse(form.is_valid())


class ExtrasFormTests(TestCase):
    def test_login_form(self):
        form = ExtrasForm({
            'user': '1',
            'house': '51',
            'street': 'Test Street',
            'city': 'Testville',
            'postcode': 'TE1 1ST',
        })
        self.assertTrue(form.is_valid())

    def test_login_form_fails_with_missing_house(self):
        form = ExtrasForm({
            'user': '1',
            'street': 'Test Street',
            'city': 'Testville',
            'postcode': 'TE1 1ST',
        })
        self.assertFalse(form.is_valid())

    def test_login_form_fails_with_missing_street(self):
        form = ExtrasForm({
            'user': '1',
            'house': '51',
            'city': 'Testville',
            'postcode': 'TE1 1ST',
        })
        self.assertFalse(form.is_valid())

    def test_login_form_fails_with_missing_city(self):
        form = ExtrasForm({
            'user': '1',
            'house': '51',
            'street': 'Test Street',
            'postcode': 'TE1 1ST',
        })
        self.assertFalse(form.is_valid())

    def test_login_form_fails_with_missing_postcode(self):
        form = ExtrasForm({
            'user': '1',
            'house': '51',
            'street': 'Test Street',
            'city': 'Testville',
        })
        self.assertFalse(form.is_valid())

    def test_login_form_fails_with_too_long_postcode(self):
        form = ExtrasForm({
            'user': '1',
            'house': '51',
            'street': 'Test Street',
            'city': 'Testville',
            'postcode': 'TE1 1STTT',
        })
        self.assertFalse(form.is_valid())

    def test_login_form_fails_with_too_long_house(self):
        form = ExtrasForm({
            'user': '1',
            'house': 'This house name is too long',
            'street': 'Test Street',
            'city': 'Testville',
            'postcode': 'TE1 1ST',
        })
        self.assertFalse(form.is_valid())

    def test_login_form_fails_with_too_long_street(self):
        form = ExtrasForm({
            'user': '1',
            'house': '51',
            'street': 'Test Street name is just way way toooooooooooo long',
            'city': 'Testville',
            'postcode': 'TE1 1ST',
        })
        self.assertFalse(form.is_valid())

    def test_login_form_fails_with_too_long_city(self):
        form = ExtrasForm({
            'user': '1',
            'house': '51',
            'street': 'Test Street',
            'city': 'Test city name is just way way toooooooooooooo long',
            'postcode': 'TE1 1ST',
        })
        self.assertFalse(form.is_valid())
