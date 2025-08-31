from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.ec_checkout, name='ec_checkout'),
    path(
        'checkout_success/<ec_order_number>',
        views.checkout_success,
        name='checkout_success',
    ),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data',
    ),
    path('wh/', webhook, name='webhook'),
]
