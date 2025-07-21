from django.urls import path
from . import views

urlpatterns = [
    path('ec_product/<int:ec_product_id>/', views.product_faq_list, name='product_faq_list'),
    path('add/<int:ec_product_id>/', views.add_faq_to_product, name='add_faq_to_product'),

]
 