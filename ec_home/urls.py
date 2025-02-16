from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.index, name='ec_home')
]


