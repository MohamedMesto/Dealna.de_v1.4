from django.shortcuts import render, redirect, reverse
from django.contrib import messages



from .forms import EC_OrderForm
def ec_checkout(request):
    ec_bag = request.session.get('ec_bag', {})
    if not ec_bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('ec_products'))
    ec_order_form = EC_OrderForm()
    template = 'ec_checkout/ec_checkout.html'
    context = {
        'ec_order_form': ec_order_form,
        'stripe_public_key': 'pk_test_51Qssd1Qfo7m0m0E99UQVWBcPAzWUNzwTIsIlSXPi4W2BQOHIHOk8K2ipqyWTWj4TlpBuNvfVRvasx4I2XikuKjMA00xyhq6okC',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)