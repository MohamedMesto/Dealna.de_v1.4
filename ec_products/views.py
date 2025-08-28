from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import EC_Product,EC_Category
from .forms import EC_ProductForm
from review.forms import ReviewForm
from faq.models import FAQ  

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



@login_required
def add_ec_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))


    
    if request.method == 'POST':
        form = EC_ProductForm(request.POST, request.FILES)
        if form.is_valid():
            ec_product=form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('ec_product_detail', args=[ec_product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = EC_ProductForm()
        
    template = 'ec_products/add_ec_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_ec_product(request, ec_product_id):
    """ Edit a ec_product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    ec_product = get_object_or_404(EC_Product, pk=ec_product_id)
    if request.method == 'POST':
        form = EC_ProductForm(request.POST, request.FILES, instance=ec_product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated ec_product!')
            return redirect(reverse('ec_product_detail', args=[ec_product.id]))
        else:
            messages.error(request, 'Failed to update ec_product. Please ensure the form is valid.')
    else:
        form = EC_ProductForm(instance=ec_product)
        messages.info(request, f'You are editing {ec_product.name}')

    template = 'ec_products/edit_ec_product.html'
    context = {
        'form': form,
        'ec_product': ec_product,
    }

    return render(request, template, context)



@login_required
def delete_ec_product(request, ec_product_id):
    """ Delete a ec_product from the store """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    ec_product = get_object_or_404(EC_Product, pk=ec_product_id)
    ec_product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('ec_products'))


# Review app
 
def ec_product_detail(request, ec_product_id):
    ec_product = get_object_or_404(EC_Product, pk=ec_product_id)
    reviews = ec_product.reviews.all()
    faqs = ec_product.faqs.all()  # related_name='faqs' in FAQ model

    user_has_reviewed = False
    if request.user.is_authenticated:
        user_has_reviewed = reviews.filter(user=request.user).exists()



    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ec_product = ec_product
            review.user = request.user
            review.save()
            return redirect('ec_product_detail', ec_product_id=ec_product.pk)
    else:
        form = ReviewForm()

    return render(request, 'ec_products/ec_product_detail.html', {
        'ec_product': ec_product,
        'reviews': reviews,
        'form': form,
        'faqs': faqs,
        "user_has_reviewed": user_has_reviewed,
    })


 