from django.contrib import admin

# Import Models
from products.models import Category
from products.models import SubCategory
from products.models import Product
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
    list_display = ('product_id', 'product_name', 'sub_catagory_1', 'sub_catagory_2', 'sub_catagory_3', 'product_price',  'stock',)
    search_fields = ('product_id', 'product_name', 'sub_catagory_1', 'sub_catagory_2', 'sub_catagory_3', 'product_price',  'stock',)
    list_per_page = 50


@admin.register(ProductBatch)
class ProductBatchAdmin(admin.ModelAdmin):
    list_display = ('batch_no', 'product', 'quantity', 'purchase_price', 'mfg_date', 'expire_date', )
    search_fields = ('batch_no', 'product', 'quantity', 'purchase_price', 'mfg_date', 'expire_date', )
    list_per_page = 50