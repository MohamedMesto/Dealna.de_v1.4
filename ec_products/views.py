from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import EC_Product,EC_Category
from .forms import EC_ProductForm


# Create your views here.

def all_ec_products(request):
    """ A view to show all ec products, including sorting and search queries """

    ec_products = EC_Product.objects.all()
    query = None
    ec_categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                ec_products = ec_products.annotate(lower_name=Lower('name'))
            if sortkey == 'ec_category':
                sortkey = 'ec_category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            ec_products = ec_products.order_by(sortkey)
            
        if 'ec_category' in request.GET:
            ec_categories = request.GET['ec_category'].split(',')
            ec_products = ec_products.filter(ec_category__name__in=ec_categories)
            ec_categories = EC_Category.objects.filter(name__in=ec_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('ec_products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            ec_products = ec_products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'ec_products': ec_products,
        'search_term': query,
        'current_ec_categories': ec_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'ec_products/ec_products.html', context)

def ec_product_detail(request, ec_product_id):
    """ A view to show individual product details """

    ec_product = get_object_or_404(EC_Product, pk=ec_product_id)

    context = {
        'ec_product': ec_product,
    }
    return render(request, 'ec_products/ec_product_detail.html', context)

def add_ec_product(request):
    """ Add a product to the store """
    
    if request.method == 'POST':
        form = EC_ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_ec_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = EC_ProductForm()
        
    template = 'ec_products/add_ec_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)