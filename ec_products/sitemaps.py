from django.contrib.sitemaps import Sitemap
from .models import EC_Product

class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return EC_Product.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at


  


# class CategorySitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.7

#     def items(self):
#         return EC_Category.objects.all()
