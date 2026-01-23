from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return [
            'ec_home',
            'ec_products',
            'newsletter:newsletter',
        ]

    def location(self, item):
        return reverse(item)
