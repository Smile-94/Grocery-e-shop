from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from accounts.models import User
from deleveryman.models import DeleveryManInfo



@receiver(post_save, sender=User)
def create_deleveryman_info(sender, instance, created, *args, **kwargs):
    if created and instance.is_deleveryman:
        DeleveryManInfo.objects.create(info_of=instance)


@receiver(post_save, sender=User)
def save_deleveryman_info(sender, instance, *args, **kwargs):
    if instance.is_deleveryman:
        instance.deleveryman_info.save()