from django.test import TestCase
from django.urls import reverse
from newsletter.models import NewsletterSubscription


class NewsletterSubscriptionTests(TestCase):
    def setUp(self):
        self.email = "test@example.com"
        self.sub = NewsletterSubscription.objects.create(
            email=self.email,
            is_active=True
        )
        self.token = self.sub.unsubscribe_token

    def test_unsubscribe_redirects(self):
        """The unsubscribe URL should redirect instead of error."""
        url = reverse("newsletter:unsubscribe", args=[self.token])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertIn("/", response.url)

    def test_unsubscribe_marks_inactive(self):
        """Unsubscribing sets is_active=False. Subscription is not deleted."""
        url = reverse("newsletter:unsubscribe", args=[self.token])
        self.client.get(url)

        sub = NewsletterSubscription.objects.get(email=self.email)
        self.assertFalse(sub.is_active)
