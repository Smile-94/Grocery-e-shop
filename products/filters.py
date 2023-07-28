import django_filters
from django import forms

# Models
from products.models import Category
from products.models import SubCategory
from products.models import Product


class CategoryFilters(django_filters.FilterSet):
    category_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ('category_name','category_location')


class SubCategoryFilters(django_filters.FilterSet):
    subcategory_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = SubCategory
        fields = ('subcategory_name','category')


class ProductFilter(django_filters.FilterSet):

    product_id = django_filters.CharFilter(
        lookup_expr='icontains',
        label="Product ID",
        widget=forms.TextInput(attrs={'placeholder': 'product ID'}),
    )
    product_name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'product name'}),
    )


    class Meta:
        model = Product
        fields = ('product_id','product_name', )
    
        