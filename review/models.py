from django.db import models
from django.contrib.auth.models import User
from ec_products.models import EC_Product
from django.core.exceptions import ValidationError
from django.utils import timezone

class ReviewModel(models.Model):
    ec_product = models.ForeignKey(EC_Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.user.username} on {self.ec_product.name}"
    

    class Meta:
        ordering = ['-id']
        unique_together = ('ec_product', 'user') # still prevents duplicates at DB level
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
