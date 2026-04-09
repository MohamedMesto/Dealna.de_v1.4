from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import EC_UserProfile
from .forms import EC_UserProfileForm

from ec_checkout.models import EC_Order


@login_required
def ec_profile(request):
    """ Display the user's ec_profile. """
    ec_profile = get_object_or_404(EC_UserProfile, user=request.user)

    if request.method == 'POST':
        form = EC_UserProfileForm(request.POST, instance=ec_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid.')

    else:
        form = EC_UserProfileForm(instance=ec_profile)
    ec_orders = ec_profile.ec_orders.all()

    template = 'ec_profiles/ec_profile.html'
    context = {
        'form': form,
        'ec_orders': ec_orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def ec_order_history(request, ec_order_number):
    ec_order = get_object_or_404(EC_Order, ec_order_number=ec_order_number)

    messages.info(request, (
        f'This is a past confirmation for ec_order number {ec_order_number}. '
        'A confirmation email was sent on the ec_order date.'
    ))

    template = 'ec_checkout/checkout_success.html'
    context = {
        'ec_order': ec_order,
        'from_ec_profile': True,
    }

    return render(request, template, context)
