from django.urls import path
from . import views
urlpatterns = [
    path('', views.ec_checkout, name='ec_checkout')
]