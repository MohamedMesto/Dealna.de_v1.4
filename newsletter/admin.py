from django.contrib import admin

from .models import NewsletterSubscription


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    """Admin configuration for the NewsletterSubscription model."""
    list_display = (
        "email",
        "is_active",
        "discount_code",
        "discount_expires",
    )
    search_fields = ("email", "discount_code")
