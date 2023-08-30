import django_filters
from django import forms
from datetime import datetime

from accounts.models import User
from products.models import Order

class EmployeeListFilter(django_filters.FilterSet):

    email = django_filters.CharFilter(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = {
            'email': {'exact'},
        }


class ReportFilter(django_filters.FilterSet):

    from_date = django_filters.DateFilter(field_name='ordered_at', lookup_expr='gte')
    to_date = django_filters.DateFilter(field_name='ordered_at', lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['from_date','to_date']