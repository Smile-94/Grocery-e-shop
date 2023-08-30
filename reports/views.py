from django.shortcuts import render
from django_xhtml2pdf.views import PdfMixin
import datetime

from django.db.models import F

# Create your views here.
# for generating pdf
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.conf import settings

# Models
from products.models import Order
from products.models import Product


class OrderListPdfView(PdfMixin, DetailView):
    model = Order
    context_object_name = 'orders'
    template_name = "report/order_report.html"  # Create a new template for the list view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['static_url'] = self.request.build_absolute_uri(settings.STATIC_URL)
        context['orders'] = Order.objects.filter(ordered=True, order_confirm=True, delevery_status=True).order_by('-id')  # Pass the queryset of all orders to the context
        context['date'] = datetime.date.today()
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = None  # Set object to None since it's not used in the template
        context = self.get_context_data()
        response = self.render_to_response(context)
        filename = "orders_report.pdf"  # Change the filename as you desire
        response['Content-Disposition'] = 'filename="{}"'.format(filename)
        return response
    

class StockListPdfView(PdfMixin, DetailView):
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
    template_name = "report/stock_report.html"  # Create a new template for the list view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['static_url'] = self.request.build_absolute_uri(settings.STATIC_URL)
        context['orders'] = self.queryset
        context['date'] = datetime.date.today()
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = None  # Set object to None since it's not used in the template
        context = self.get_context_data()
        response = self.render_to_response(context)
        filename = "stock_report.pdf"  # Change the filename as you desire
        response['Content-Disposition'] = 'filename="{}"'.format(filename)
        return response