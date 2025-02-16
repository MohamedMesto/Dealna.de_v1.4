from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import EC_OrderForm
from .models import EC_Order, EC_OrderLineItem
from ec_products.models import EC_Product
import os
from ec_bag.contexts import ec_bag_contents

import stripe

def ec_checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        ec_bag = request.session.get('ec_bag', {})
    
     
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        ec_order_form = EC_OrderForm(form_data)
        if ec_order_form.is_valid():
            ec_order = ec_order_form.save()
            for item_id, item_data in ec_bag.items():
                try:
                    ec_product = EC_Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        ec_order_line_item = EC_OrderLineItem(
                            ec_order=ec_order,
                            ec_product=ec_product,
                            quantity=item_data,
                        )
                        ec_order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            ec_order_line_item = EC_OrderLineItem(
                                ec_order=ec_order,
                                ec_product=ec_product,
                                quantity=quantity,
                                ec_product_size=size,
                            )
                            ec_order_line_item.save()
                except EC_Product.DoesNotExist:
                    messages.error(request, (
                        "One of the ec_products in your ec_bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    ec_order.delete()
                    return redirect(reverse('view_ec_bag'))

        

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[ec_order.ec_order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                            Please double check your information.')
    else:
        ec_bag = request.session.get('ec_bag', {})
        if not ec_bag:
            messages.error(request, "There's nothing in your ec_bag at the moment")
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
       ## 'client_secret': intent.stripe_secret_key,
        'client_secret': intent.client_secret,
    }
    
    return render(request, template, context)


def checkout_success(request, ec_order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    ec_order = get_object_or_404(EC_Order, ec_order_number=ec_order_number)
    messages.success(request, f'EC_Order successfully processed! \
        Your ec_order number is {ec_order_number}. A confirmation \
        email will be sent to {ec_order.email}.')
    if 'ec_bag' in request.session:
        del request.session['ec_bag']
    template = 'ec_checkout/checkout_success.html'
    context = {
        'ec_order': ec_order,
    }
    return render(request, template, context)