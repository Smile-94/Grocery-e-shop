from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

# Create your models here.

class BillingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shipping_address')
    address = models.CharField( max_length=250, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    city  = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.user)
    

    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]

        for field_name in field_names:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False
        return True
    
    class Meta:
        verbose_name_plural = 'Billing Addresses'
