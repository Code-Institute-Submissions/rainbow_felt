from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import show


# Test show cart page
class ShowPagePageTest(TestCase):
    def test_show_cart_page(self):
        # Make sure page resolves
        showcart_page = resolve('/shopping-cart/show/')
        self.assertEqual(showcart_page.func, show)

        # Make sure correct template used
        showcartc = self.client.get('/shopping-cart/show/')
        self.assertTemplateUsed(showcartc, "show-cart.html")

