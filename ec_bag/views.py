from django.shortcuts import redirect, render

# Create your views here.

def view_ec_bag(request):
    """ A view to renders the ec_bag contents page """

    return render(request, 'ec_bag/ec_bag.html')


def add_to_ec_bag(request, item_id):
    """ Add a quantity of the specified ec_product to the shopping ec_bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    ec_bag = request.session.get('ec_bag', {})

    if item_id in list(ec_bag.keys()):
        ec_bag[item_id] += quantity
    else:
        ec_bag[item_id] = quantity

    request.session['ec_bag'] = ec_bag
    print(request.session['ec_bag'])
    return redirect(redirect_url)
    