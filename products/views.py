# Imports
from django.shortcuts import render, get_object_or_404
from .models import Product


# View all products in one page
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


# View each product individually
def product_view(request, id):
    viewed_product = get_object_or_404(Product, pk=id)
    return render(request, 'productdetails.html', {'viewed_product': viewed_product})
