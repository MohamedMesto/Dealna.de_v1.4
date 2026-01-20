from django.urls import path
from . import views

app_name = "newsletter"

urlpatterns = [
    # Main newsletter page or form
    path("", views.newsletter, name="newsletter"),

    # Unsubscribe link with secure token
    path("unsubscribe/<str:token>/", views.unsubscribe, name="unsubscribe"),
]
