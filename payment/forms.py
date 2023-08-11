from django import forms

# Models
from payment.models import BillingAddress

class BillingAddressForm(forms.ModelForm):

    class Meta:
        model = BillingAddress
        exclude = ('user',)