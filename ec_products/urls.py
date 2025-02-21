from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_ec_products, name='ec_products'),
    path('<int:ec_product_id>/', views.ec_product_detail, name='ec_product_detail'),
    path('add/', views.add_ec_product, name='add_ec_product'),
    path('edit/<int:ec_product_id>/', views.edit_ec_product, name='edit_ec_product'),
    path('delete/<int:ec_product_id>/', views.delete_ec_product, name='delete_ec_product'),
]

 