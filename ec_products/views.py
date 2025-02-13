from django.shortcuts import render
from .models import EC_Product

# Create your views here.

def all_ec_products(request):
    """ A view to show all ec products, including sorting and search queries """

    ec_products = EC_Product.objects.all()

    context = {
        'ec_products': ec_products,
    }

    return render(request, 'ec_products/ec_products.html', context)