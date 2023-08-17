from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

# Import Generic View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import UpdateView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from customer.permissions import CustomerPassesTestMixin

# Import Models
from accounts.models import Profile
from accounts.forms import ProfileForm
from authority.models import ShippingCharge
from products.models import Order




# Create your views here.
class CustomerHomeView(LoginRequiredMixin,CustomerPassesTestMixin, TemplateView):
    template_name = 'customer/customer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Customer Panel" 
        context["orders"] = Order.objects.filter(user=self.request.user, ordered=True).order_by('-id')[:10]
        context["pending_order"] = Order.objects.filter(user=self.request.user, ordered=True, order_confirm=False).count()
        context["confirmed_order"] = Order.objects.filter(user=self.request.user, ordered=True, order_confirm=True).count()
        context["total_orders"] = Order.objects.filter(user=self.request.user, ordered=True).count()
        return context
    

class MyOrderListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'customer/pending_order.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user, ordered=True, order_confirm=False).order_by('id')[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "My order"
        context["shipping_charge"] = ShippingCharge.objects.latest('id')
        return context
    

class MyConfirmedOrderListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'customer/confirmed_order.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user, ordered=True, order_confirm=True).order_by('id')[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "My order"
        context["shipping_charge"] = ShippingCharge.objects.latest('id')
        return context

class AddProfileInfo(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'customer/customer_profile.html'
    success_url = reverse_lazy('customer:customer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Add/Edit Profile'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Profile Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, "Some thing Wron! Try agning")
        return super().form_invalid(form)