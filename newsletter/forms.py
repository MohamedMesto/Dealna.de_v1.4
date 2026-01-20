from django import forms

from .models import NewsletterSubscription


class NewsletterForm(forms.ModelForm):
    """Form for newsletter subscription."""
    class Meta:
        model = NewsletterSubscription
        fields = ["email"]
