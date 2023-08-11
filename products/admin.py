from django.contrib import admin

# Import Models
from products.models import Category
from products.models import SubCategory
from products.models import Product
from products.models import Cart
from products.models import Order
from products.models import ProductBatch




# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_location', 'created_at', 'updated_at' )
    search_fields = ('category_name', 'category_location', )
    list_per_page = 50


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory_name', 'category', 'created_at', 'updated_at')
    search_fields = ('subcategory_name', 'category', )
    list_per_page = 50


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'sub_catagory_1', 'sub_catagory_2', 'sub_catagory_3', 'product_price', 'stock',)
    search_fields = ('product_id', 'product_name', 'sub_catagory_1', 'sub_catagory_2', 'sub_catagory_3', 'product_price', 'stock',)
    list_per_page = 50

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'sub_catagory_1':
            kwargs['queryset'] = SubCategory.objects.filter(is_active=True)
        elif db_field.name == 'sub_catagory_2':
            kwargs['queryset'] = SubCategory.objects.filter(is_active=True)
        elif db_field.name == 'sub_catagory_3':
            kwargs['queryset'] = SubCategory.objects.filter(is_active=True)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Cart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ('user', 'quentity', 'purchased', 'created', 'updated', )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('ordered_id', 'user', 'ordered', 'created', 'payment_id', 'order_id', 'payment_status', 'order_confirm', 'ordered_at', 'confirmed_at', 'delevery_status', )

@admin.register(ProductBatch)
class ProductBatchAdmin(admin.ModelAdmin):
    list_display = ('batch_no', 'product', 'quantity', 'purchase_price', 'mfg_date', 'expire_date', )
    search_fields = ('batch_no', 'product', 'quantity', 'purchase_price', 'mfg_date', 'expire_date', )
    list_per_page = 50