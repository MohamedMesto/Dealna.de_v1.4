from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    list_display = ('ec_product', 'question', 'created_at')
    list_filter = ('ec_product',)


admin.site.register(FAQ, FAQAdmin)
