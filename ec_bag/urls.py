from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_ec_bag, name='view_ec_bag'),
    path('add/<item_id>/', views.add_to_ec_bag, name='add_to_ec_bag'),
]