from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_ec_products, name='ec_products')
]