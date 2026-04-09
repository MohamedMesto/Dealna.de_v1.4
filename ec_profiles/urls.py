from django.urls import path
from . import views
urlpatterns = [
    path('', views.ec_profile, name='ec_profile'),
    path(
        'ec_order_history/<ec_order_number>',
        views.ec_order_history, name='ec_order_history'),
]
