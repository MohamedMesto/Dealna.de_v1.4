from django.shortcuts import render, get_object_or_404, redirect
from .models import FAQ
from ec_products.models import EC_Product
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import FAQForm
 


def product_faq_list(request, ec_product_id):
    ec_product = get_object_or_404(EC_Product, pk=ec_product_id)
    faqs = FAQ.objects.filter(ec_product=ec_product)

    return render(request, 'faq/product_faq_list.html', {
        'ec_product': ec_product,
        'faqs': faqs,
    })



@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_product_faq(request, ec_product_id):
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
     
     
def edit_product_faq(request, faq_id):
    faq = get_object_or_404(FAQ, pk=faq_id)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('ec_product_detail', ec_product_id=faq.ec_product.id)
    else:
        form = FAQForm(instance=faq)
    return render(request, 'faq/edit_faq.html', {'form': form, 'faq': faq})

def delete_product_faq(request, faq_id):
    faq = get_object_or_404(FAQ, pk=faq_id)
    if request.method == 'POST':
        ec_product_id = faq.ec_product.id
        faq.delete()
        return redirect('ec_product_detail', ec_product_id=ec_product_id)
    return render(request, 'faq/delete_faq.html', {'faq': faq})