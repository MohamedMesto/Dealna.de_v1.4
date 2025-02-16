from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import EC_OrderLineItem

@receiver(post_save, sender=EC_OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update ec_order total on lineitem update/create
    """
    instance.ec_order.update_total()
    
@receiver(post_delete, sender=EC_OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update ec_order total on lineitem delete
    """
    instance.ec_order.update_total()