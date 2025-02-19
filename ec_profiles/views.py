from django.shortcuts import render, get_object_or_404

from .models import EC_UserProfile

def ec_profile(request):
    """ Display the user's profile. """
    ec_profile = get_object_or_404(EC_UserProfile, user=request.user)
    template = 'ec_profiles/ec_profile.html'
    context = {
    'ec_profile': ec_profile,
    }
    return render(request, template, context)