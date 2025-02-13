from django.shortcuts import render, get_object_or_404
from .models import EC_Product

# Create your views here.

def all_ec_products(request):
    """ A view to show all ec products, including sorting and search queries """

    ec_products = EC_Product.objects.all()

    context = {
        'ec_products': ec_products,
    }

    return render(request, 'ec_products/ec_products.html', context)


def ec_product_detail(request, ec_product_id):
    """ A view to show individual product details """

    ec_product = get_object_or_404(EC_Product, pk=ec_product_id)

    context = {
        'ec_product': ec_product,
    }

    return render(request, 'ec_products/ec_product_detail.html', context)