from django.contrib import admin
from .models import EC_Category, EC_Product



class EC_ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'ec_category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class EC_CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
 



# Register your models here.
admin.site.register(EC_Product, EC_ProductAdmin)
admin.site.register(EC_Category, EC_CategoryAdmin)