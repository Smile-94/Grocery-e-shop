# Generated by Django 4.2.2 on 2023-07-14 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_rename_modified_at_billingaddress_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
