from django.urls import path
from . import views
urlpatterns = [
    path('', views.ec_profile, name='ec_profile')
]