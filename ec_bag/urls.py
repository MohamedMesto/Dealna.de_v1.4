from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_ec_bag, name='view_ec_bag')
]