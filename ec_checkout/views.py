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
    }
    return render(request, template, context)