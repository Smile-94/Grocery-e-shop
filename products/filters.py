import django_filters
from django import forms

# Models
from products.models import Category
from products.models import SubCategory
from products.models import Product
from products.models import Order


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


class OrderFilter(django_filters.FilterSet):
    from_date = django_filters.DateFilter(field_name='ordered_at', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}), label='From')
    to_date = django_filters.DateFilter(field_name='ordered_at', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}), label='To')

    class Meta:
        model = Order
        fields = ['from_date','to_date']
    
        