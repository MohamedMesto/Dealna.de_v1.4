from django.db import models
from ec_products.models import EC_Product  # import your product model


class FAQ(models.Model):
    ec_product = models.ForeignKey(
        EC_Product, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ec_product.name} - {self.question}"
