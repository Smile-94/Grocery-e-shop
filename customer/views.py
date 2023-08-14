from django.shortcuts import render

# Import Generic View
from django.views.generic import TemplateView
from django.views.generic import ListView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from customer.permissions import CustomerPassesTestMixin

# Import Models
from authority.models import ShippingCharge
from products.models import Order




# Create your views here.
class CustomerHomeView(LoginRequiredMixin,CustomerPassesTestMixin, TemplateView):
    template_name = 'customer/customer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Admin Panel" 
        
        return context
    

class MyOrderListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'customer/pending_order.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user, ordered=True).order_by('id')[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "My order"
        context["shipping_charge"] = ShippingCharge.objects.latest('id')
        return context

