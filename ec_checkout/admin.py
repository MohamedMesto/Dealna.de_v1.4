from django.contrib import admin

from .models import EC_Order, EC_OrderLineItem
# Register your models here.

 
class EC_OrderLineItemAdminInline(admin.TabularInline):
    model = EC_OrderLineItem
    readonly_fields = ('lineitem_total',)
class EC_OrderAdmin(admin.ModelAdmin):
    inlines = (EC_OrderLineItemAdminInline,)
    readonly_fields = ('ec_order_number', 'date',
                       'delivery_cost', 'ec_order_total',
                       'grand_total',)
    fields = ('ec_order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'ec_order_total', 'grand_total',)
    list_display = ('ec_order_number', 'date', 'full_name',
                    'ec_order_total', 'delivery_cost',
                    'grand_total',)
    ec_ordering = ('-date',)
admin.site.register(EC_Order, EC_OrderAdmin)