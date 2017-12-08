# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from carton.cart import Cart
from orders.models import Order


# Create your views here.
@login_required
@csrf_exempt
def paypal_return(request):

    # Get cart session and create vars
    cart = Cart(request.session)
    cartlist = cart.cart_serializable
    paypal = cart.paypal_form.initial

    # Find item and quantity ordered in nested dictionaries and save to orders db
    for item, v in cartlist.iteritems():
        if 'quantity' in v:
            order_entry = Order(user=request.user, invoice=paypal['invoice'], items=int(item), quantities=v['quantity'])
            order_entry.save()

    # Clear cart after making order
    cart.clear()

    return render(request, 'paypal/paypal_return.html')


# Send message to user to confirm cancellation of purchase
@login_required
def paypal_cancel(request):	
    messages.success(request, 'You have cancelled your payment.')
    return redirect('shopping-cart-show')
