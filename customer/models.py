from django.db import models

# Abstract Base Models
from accounts.models import BaseModels

# Import Models
from accounts.models import User

# Create your models here.

#Customer Billing Address
class BillingAddress(BaseModels):
    address_of = models.OneToOneField(User, on_delete=models.CASCADE, related_name='billing_user')
    address = models.CharField(max_length=200, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True, default='Bangladesh')
    post_code = models.CharField(max_length=50,blank=True, null=True)


# Customer Shipping Address
class ShippingAddress(BaseModels):
    address_of = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shipping_user')
    receiver_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True, default='Bangladesh')
    post_code = models.CharField(max_length=50,blank=True, null=True)
