# Generated by Django 4.2.2 on 2023-07-11 17:17

import common.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('category_location', models.CharField(choices=[('bodycare', 'Bodycare'), ('food', 'Food')], default='food', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subcategory_name', models.CharField(max_length=50, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_id', models.CharField(blank=True, max_length=50, null=True)),
                ('product_name', models.CharField(max_length=200)),
                ('purchase_price', models.FloatField(blank=True, default=None, null=True, validators=[common.validators.validate_float_value])),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/product')),
                ('product_price', models.FloatField(blank=True, default=None, null=True, validators=[common.validators.validate_float_value])),
                ('unit', models.CharField(blank=True, max_length=700, null=True)),
                ('stock', models.PositiveBigIntegerField(default=0)),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('sub_catagory_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categries_1', to='products.subcategory')),
                ('sub_catagory_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categries_2', to='products.subcategory')),
                ('sub_catagory_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categries_3', to='products.subcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
