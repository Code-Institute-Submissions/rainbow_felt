# Imports
from django.db import models


# Create model for products
class Product(models.Model):
    name = models.CharField(max_length=60, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='static/product_images/', default='static/product_images/bracelet1.jpg')
