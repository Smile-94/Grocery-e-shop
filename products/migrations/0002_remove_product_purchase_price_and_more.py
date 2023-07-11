# Generated by Django 4.2.2 on 2023-07-11 18:20

import common.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='purchase_price',
        ),
        migrations.AlterField(
            model_name='category',
            name='category_location',
            field=models.CharField(choices=[('bodycare', 'Bodycare'), ('private_Care', 'Private Care'), ('food', 'Food')], default='food', max_length=20),
        ),
        migrations.CreateModel(
            name='ProductBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('batch_no', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('purchase_price', models.FloatField(blank=True, default=None, null=True, validators=[common.validators.validate_float_value])),
                ('mfg_date', models.DateTimeField(blank=True, null=True)),
                ('expire_date', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch_product', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]