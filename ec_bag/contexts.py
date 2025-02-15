from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from ec_products.models import EC_Product

def ec_bag_contents(request):

    ec_bag_items = []
    total = 0
    ec_product_count = 0
    ec_bag = request.session.get('ec_bag', {})

    for item_id, quantity in ec_bag.items():
        ec_product = get_object_or_404(EC_Product, pk=item_id)
        total += quantity * ec_product.price
        ec_product_count += quantity
        ec_bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'ec_product': ec_product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'ec_bag_items': ec_bag_items,
        'total': total,
        'ec_product_count': ec_product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context