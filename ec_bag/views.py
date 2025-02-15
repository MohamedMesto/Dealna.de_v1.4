from django.shortcuts import render

# Create your views here.

def view_ec_bag(request):
    """ A view to renders the ec_bag contents page """

    return render(request, 'ec_bag/ec_bag.html')