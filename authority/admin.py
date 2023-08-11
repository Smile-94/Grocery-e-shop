from django.contrib import admin

#Import Models
from authority.models import ShippingCharge

# Register your models here.
@admin.register(ShippingCharge)
class ShippingChargeAdmin(admin.ModelAdmin):
    list_display = ('shipping_charge', 'created_at', 'modified_at', )
