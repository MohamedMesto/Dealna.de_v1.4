from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import EC_OrderForm
import os

from ec_bag.contexts import ec_bag_contents

import stripe

 
 
def ec_checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    ec_bag = request.session.get('ec_bag', {})
    if not ec_bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('ec_products'))
    
    current_ec_bag = ec_bag_contents(request)
    total = current_ec_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    ec_order_form = EC_OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'ec_checkout/ec_checkout.html'
    context = {
        'ec_order_form': ec_order_form,

        'stripe_public_key': stripe_public_key,
        'client_secret': stripe_secret_key,

        ##### 'client_secret': intent.client_secret,
    }
    
    return render(request, template, context)