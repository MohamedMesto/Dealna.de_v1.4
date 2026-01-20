from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    unsubscribe_token = models.CharField(max_length=50, blank=True)
    discount_code = models.CharField(max_length=20, default="WELCOME10")
    discount_expires = models.DateTimeField(blank=True, null=True)
    discount_used = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Generate unique unsubscribe token if not set
        if not self.unsubscribe_token:
            self.unsubscribe_token = get_random_string(32)
        # Always use the 10% code
        self.discount_code = "WELCOME10"
        # Set expiration date to 2 months from now
        if not self.discount_expires:
            self.discount_expires = timezone.now() + timedelta(days=60)
        super().save(*args, **kwargs)

    def discount_valid(self):
        """Return True if the discount is still valid and unused."""
        return (
            not self.discount_used
            and self.discount_expires
            and self.discount_expires > timezone.now()
        )

    def mark_discount_used(self):
        """Mark the discount as used once applied."""
        self.discount_used = True
        self.save()

    def __str__(self):
        return self.email
