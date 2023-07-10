from django.contrib import admin

#Import Models
from customer.models import BillingAddress
from customer.models import ShippingAddress

# Register your models here.
@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('address_of', 'address', 'contact_number', 'city', 'country', 'post_code', )
    search_fields = ('address_of', 'address', 'contact_number', 'city', 'country', 'post_code', )
    list_per_page= 50


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('address_of', 'receiver_name', 'address', 'contact_number', 'city', 'country', 'post_code', )
    search_fields = ('address_of', 'receiver_name', 'address', 'contact_number', 'city', 'country', 'post_code', )
    list_per_page = 50