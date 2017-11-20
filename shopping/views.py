from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from carton.cart import Cart
from products.models import Product


def add(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('id'))
    cart.add(product, price=product.price)
    messages.success(request, 'The item has been added to your cart.')
    return redirect('all_products')


def remove(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('id'))
    cart.remove(product)
    return redirect('shopping-cart-show')


def show(request):
    return render(request, 'show-cart.html')
