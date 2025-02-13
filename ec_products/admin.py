from django.contrib import admin
from .models import EC_Category, EC_Product

# Register your models here.
admin.site.register(EC_Product)
admin.site.register(EC_Category)