from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib import messages

from carton.cart import Cart
from products.models import Product


# Add item to cart and redirect user back to main products page
def add(request):
    cart = Cart(request.session)  # Get cart session
    # Get product, raise error if doesn't exist
    try:
        product = Product.objects.get(id=request.GET.get('id'))
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    cart.add(product, price=product.price)  # Add item to cart
    messages.success(request, 'The item has been added to your cart.')  # Msg for success
    return redirect('all_products')


# Remove item from cart
def remove(request):
    cart = Cart(request.session)  # Get cart session
    # Get product, raise error if doesn't exist
    try:
        product = Product.objects.get(id=request.GET.get('id'))
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    cart.remove(product)  # Remove item from cart
    return redirect('shopping-cart-show')  # Refresh page so item is no longer shown


# Show users cart
def show(request):
    return render(request, 'show-cart.html')
