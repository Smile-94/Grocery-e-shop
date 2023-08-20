from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from datetime import datetime

from django.db.models import F

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Generic Classes
from django.views.generic import ListView
from django.views.generic import DetailView



# Models 
from products.models import Order
from products.models import Product


# Forms
from authority.forms import ConfirmDeleveryForm
from products.forms import OrderConfirmForm

from products.filters import OrderFilter


class ReportOrderView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Order
    queryset = Order.objects.filter(ordered=True, order_confirm=True, delevery_status=True).order_by('-id')
    context_object_name = 'orders'
    template_name = 'authority/oders_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Confirmed Order List" 
        return context


class StockReportView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Product
    queryset = Product.objects.filter(is_active=True).values('id').annotate(
        product_category= F('sub_catagory_1__category__category_name'),
        total_price = F('stock')*F('product_price')

    ).values(
        'product_id',
        'product_name',
        'product_category',
        'unit',
        'stock',
        'product_price',
        'total_price'
    ).order_by('-id')
    context_object_name = 'orders'
    template_name = 'authority/stock_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Confirmed Order List" 
        return context