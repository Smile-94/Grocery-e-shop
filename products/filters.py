import django_filters

# Models
from products.models import Category
from products.models import SubCategory


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