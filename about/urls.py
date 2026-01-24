from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_page, name='about'),
    path("impressum/", views.impressum, name="impressum"),
]
