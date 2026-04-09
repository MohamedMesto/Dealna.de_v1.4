from django.urls import path
from . import views

urlpatterns = [
    path(
        'ec_product/<int:ec_product_id>/',
        views.product_faq_list, name='product_faq_list'),
    path(
        'add/<int:ec_product_id>/',
        views.add_product_faq, name='add_product_faq'),
    path(
        'faq/<int:faq_id>/edit/',
        views.edit_product_faq, name='edit_product_faq'),
    path(
        'faq/<int:faq_id>/delete/',
        views.delete_product_faq, name='delete_product_faq'),
]
