from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Cart


@receiver(post_save, sender=Cart)
def decrease_product_stock(sender, instance, created, **kwargs):
    if created and not instance.purchased:
        instance.items.stock -= 1
        instance.items.save()