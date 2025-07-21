from django.shortcuts import render, get_object_or_404, redirect
from .models import FAQ
from ec_products.models import EC_Product
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import FAQForm
 


def product_faq_list(request, ec_product_id):
    ec_product = get_object_or_404(EC_Product, pk=ec_product_id)
    faqs = FAQ.objects.filter(ec_product=ec_product)

    # print("Hallooooooooooo")
    # print(f"Product: {ec_product}")  # Add debug
    # print(f"FAQs found: {faqs.count()}")  # Add debug


    return render(request, 'faq/faq_list.html', {
        'ec_product': ec_product,
        'faqs': faqs,
    })

 

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_faq_to_product(request, ec_product_id):
    ec_product = get_object_or_404(EC_Product, id=ec_product_id)

    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.ec_product = ec_product
            faq.save()
            return redirect('ec_product_detail', ec_product_id=ec_product.id)
    else:
        form = FAQForm()

    return render(request, 'faq/add_faq.html', {
        'form': form,
        'ec_product': ec_product,
    })
     
     
