from django.shortcuts import render
def ec_profile(request):
    """ Display the user's profile. """
    template = 'ec_profiles/ec_profile.html'
    context = {}
    return render(request, template, context)