from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import NewsletterSubscription
from .forms import NewsletterForm


def send_welcome_email(email):
    """Send a rich HTML welcome email."""
    subject = "Welcome to Dealna.de E-Commerce Website"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [email]
    html_content = render_to_string("newsletter/welcome_email.html", {})
    msg = EmailMultiAlternatives(subject, "", from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def newsletter(request):
    """Handle newsletter signup form."""
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            subscription, _ = NewsletterSubscription.objects.get_or_create(
                email=email
            )

            # Reactivate if previously unsubscribed
            if not subscription.is_active:
                subscription.is_active = True
                subscription.save()

            # Build unsubscribe link
            unsubscribe_link = request.build_absolute_uri(
                reverse(
                    "newsletter:unsubscribe",
                    args=[subscription.unsubscribe_token],
                )
            )

            # Build welcome message
            subject = "Welcome to Dealna.de – Smart Deals Await!"

            message = (
                "Hello!\n\n"
                "Thank you for subscribing to Dealna.de 🎉\n"
                "You’re now part of our community where we share \n"
                "the best deals on"
                "electronics, accessories, and smart home essentials.\n\n"
                "As a welcome gift, here’s your exclusive 10% discount code:\n"
                f"👉 {subscription.discount_code}\n\n"
                "Use it on your next purchase before "
                f"{subscription.discount_expires.strftime('%B %d, %Y')}.\n\n"
                "As a subscriber, you’ll receive:\n"
                "- ⚡ New and trending tech deals\n"
                "- 🔥 Top discounts and clearance offers\n"
                "- 🏠 Smart home and lifestyle electronics\n"
                "- 💡 Buying tips and exclusive promotions\n\n"
                "If you ever wish to unsubscribe, you can do so here:\n"
                f"{unsubscribe_link}\n\n"
                "Best regards,\n"
                "The Dealna.de Team"
            )

            # Send confirmation email
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=True,
            )

            messages.success(
                request,
                "Thank you for subscribing! A confirmation email was sent.",
            )
            return redirect("newsletter:newsletter")
    else:
        form = NewsletterForm()

    return render(request, "newsletter/newsletter.html", {"form": form})


def unsubscribe(request, token):
    """Handle newsletter unsubscription securely."""
    try:
        subscription = NewsletterSubscription.objects.get(
            unsubscribe_token=token
        )
        if subscription.is_active:
            subscription.is_active = False
            subscription.save()
            messages.success(
                request,
                "You have been unsubscribed from the Dealna.de newsletter.",
            )
        else:
            messages.info(request, "You are already unsubscribed.")
    except NewsletterSubscription.DoesNotExist:
        messages.error(request, "Invalid unsubscribe link.")
    return redirect("ec_home")
