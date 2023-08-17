from django import forms


from products.models import Order
from authority.models import ShippingCharge


class ShippingChargeForm(forms.ModelForm):

    class Meta:
        model = ShippingCharge
        fields = ('shipping_charge',)
       
class ConfirmDeleveryForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('delevery_status',)