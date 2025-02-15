from django.apps import AppConfig


class EcCheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ec_checkout'

    def ready(self):
        import ec_checkout.signals