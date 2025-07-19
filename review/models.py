from django.db import models
from django.contrib.auth.models import User
from ec_products.models import EC_Product

class ReviewModel(models.Model):
    ec_product = models.ForeignKey(EC_Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"{self.user} on {self.ec_product}"
