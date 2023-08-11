from django.db import models

# Create your models here.

class ShippingCharge(models.Model):
    shipping_charge = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now_add=True)
