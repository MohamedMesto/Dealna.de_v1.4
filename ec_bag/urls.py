from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_ec_bag, name='view_ec_bag'),
    path('add/<item_id>/', views.add_to_ec_bag, name='add_to_ec_bag'),
    path('adjust/<item_id>/', views.adjust_ec_bag, name='adjust_ec_bag'),
    path('remove/<item_id>/', views.remove_from_ec_bag, name='remove_from_ec_bag'),
]