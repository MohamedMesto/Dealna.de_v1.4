from django.contrib import admin
from .models import EC_Order, EC_OrderLineItem


class EC_OrderLineItemAdminInline(admin.TabularInline):
    model = EC_OrderLineItem
    readonly_fields = ('lineitem_total',)


class EC_OrderAdmin(admin.ModelAdmin):
    inlines = (EC_OrderLineItemAdminInline,)
    readonly_fields = ('ec_order_number', 'date',
                       'delivery_cost', 'ec_order_total',
                       'grand_total', 'original_ec_bag',
                       'stripe_pid')
    fields = ('ec_order_number',
              'ec_user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'ec_order_total', 'grand_total', 'original_ec_bag',
              'stripe_pid')
    list_display = ('ec_order_number', 'date', 'full_name',
                    'ec_order_total', 'delivery_cost',
                    'grand_total',)
    ec_ordering = ('-date',)


admin.site.register(EC_Order, EC_OrderAdmin)
