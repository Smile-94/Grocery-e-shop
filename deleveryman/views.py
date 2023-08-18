from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

# Import Generic View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from deleveryman.permissions import DeleveryManPassesTestMixin

# Import Models
from accounts.models import Profile
from accounts.forms import ProfileForm
from authority.forms import ConfirmDeleveryForm
from authority.models import ShippingCharge
from products.models import Order




# Create your views here.
class DeleveryManHomeView(LoginRequiredMixin, DeleveryManPassesTestMixin, TemplateView):
    template_name = 'delevery_man/delevery_man.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Customer Panel" 
        context["orders"] = Order.objects.filter(assigned_to=self.request.user, ordered=True, order_confirm=True, delevery_status=False).order_by('-id')[:10]
        context["pending_order"] = Order.objects.filter(assigned_to=self.request.user, ordered=True, order_confirm=True, delevery_status=False).count()
        context["confirmed_order"] = Order.objects.filter(assigned_to=self.request.user, ordered=True, delevery_status=True).count()
        context["total_orders"] = Order.objects.filter(assigned_to=self.request.user, ordered=True,order_confirm=True ).count()
        return context


class DeleveryManPendingListView(LoginRequiredMixin, DeleveryManPassesTestMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'delevery_man/delevery_orders.html'

    def get_queryset(self):
        # Filter orders for the currently logged-in delivery man
        return Order.objects.filter(ordered=True, order_confirm=True, assigned_to=self.request.user, delevery_status=False).order_by('-id')

    def get_context_data(self, **kwargs):
        print('Query Set: ',self.queryset)
        context = super().get_context_data(**kwargs)
        context["title"] = "Pending Order List" 
        return context

class DeleveryConfirmedOrderListView(LoginRequiredMixin, DeleveryManPassesTestMixin, ListView):
    model = Order
    queryset = Order.objects.filter(ordered=True, order_confirm=True).order_by('-id')
    context_object_name = 'orders'
    template_name = 'delevery_man/delevery_orders.html'

    def get_queryset(self):
        # Filter orders for the currently logged-in delivery man
        return Order.objects.filter(ordered=True, order_confirm=True, assigned_to=self.request.user, delevery_status=True).order_by('-id')

    def get_context_data(self, **kwargs):
        print('Query Set: ',self.queryset)
        context = super().get_context_data(**kwargs)
        context["title"] = "Confirmed Order List" 
        context["form"] = ConfirmDeleveryForm
        context["confirmed"] = True 
        return context

class DeleveryManOrderDetailsView(LoginRequiredMixin, DeleveryManPassesTestMixin, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'delevery_man/delevery_orders.html'

    def get_context_data(self, **kwargs):
        shipping_charge = ShippingCharge.objects.latest('id')
        order_total = Order.objects.filter(id=self.kwargs['pk'])[0]
        context = super().get_context_data(**kwargs)
        context["title"] = 'Order Details' 
        context["details"] = True
        context["shipping_charge"] = shipping_charge
        context["total"] = order_total.get_totals()+shipping_charge.shipping_charge
        context["form"] = ConfirmDeleveryForm
        return context

class DeleveryManConfirmDeleveryView(LoginRequiredMixin, DeleveryManPassesTestMixin, UpdateView):
    model = Order
    form_class = ConfirmDeleveryForm
    template_name = 'delevery_man/delevery_orders.html'
    success_url = reverse_lazy('deleveryman:deleveryman_Confirmed_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Confirmed Delevery"
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            form_obj = form.save(commit=False)
        messages.success(self.request, "Product Delevery Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something wrong try again!")
        return super().form_invalid(form)
