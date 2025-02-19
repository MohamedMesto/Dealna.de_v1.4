from django.shortcuts import render, get_object_or_404
from django.contrib import messages


from .models import EC_UserProfile
from .forms import EC_UserProfileForm

def ec_profile(request):
    """ Display the user's ec_profile. """
    ec_profile = get_object_or_404(EC_UserProfile, user=request.user)
    if request.method == 'POST':
        form = EC_UserProfileForm(request.POST, instance=ec_profile)
        if form.is_valid():
                form.save()
        messages.success(request, 'Profile updated successfully')

    form = EC_UserProfileForm(instance=ec_profile)
    ec_orders = ec_profile.ec_orders.all()


    template = 'ec_profiles/ec_profile.html'
    context = {
        'form': form,
        'ec_orders': ec_orders,
        'on_profile_page': True
    }
    return render(request, template, context)