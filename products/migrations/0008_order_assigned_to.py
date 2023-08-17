# Generated by Django 4.2.2 on 2023-08-17 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_cart_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='assigned_to',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_deleveryman': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_man', to=settings.AUTH_USER_MODEL),
        ),
    ]