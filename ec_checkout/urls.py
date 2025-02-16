from django.urls import path
from . import views
urlpatterns = [
    path('', views.ec_checkout, name='ec_checkout'),
    path('checkout_success/<ec_order_number>', views.checkout_success, name='checkout_success'),
]