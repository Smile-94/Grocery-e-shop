from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from datetime import datetime

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Generic Classes
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Models 
from products.models import Order
from authority.models import ShippingCharge

# Forms
from authority.forms import ConfirmDeleveryForm
from products.forms import OrderConfirmForm

from products.filters import OrderFilter



class PendingListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Order
    queryset = Order.objects.filter(ordered=True, order_confirm=False).order_by('-id')
    context_object_name = 'orders'
    template_name = 'authority/order_details.html'

    def get_context_data(self, **kwargs):
        print('Query Set: ',self.queryset)
        context = super().get_context_data(**kwargs)
        context["title"] = "Pending Order List" 
        return context

class ConfirmedOrderListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Order
    queryset = Order.objects.filter(ordered=True, order_confirm=True).order_by('-id')
    context_object_name = 'orders'
    template_name = 'authority/order_details.html'

    def get_context_data(self, **kwargs):
        print('Query Set: ',self.queryset)
        context = super().get_context_data(**kwargs)
        context["title"] = "Confirmed Order List" 
        context["form"] = ConfirmDeleveryForm
        context["confirmed"] = True 
        return context


class OrderDetailsView(LoginRequiredMixin, AdminPassesTestMixin, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'authority/order_details.html'

    def get_context_data(self, **kwargs):
        shipping_charge = ShippingCharge.objects.latest('id')
        order_total = Order.objects.filter(id=self.kwargs['pk'])[0]
        context = super().get_context_data(**kwargs)
        context["title"] = 'Order Details' 
        context["details"] = True
        context["shipping_charge"] = shipping_charge
        context["total"] = order_total.get_totals()+shipping_charge.shipping_charge
        return context

class ConfirmOrderView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Order
    form_class = OrderConfirmForm
    template_name = 'authority/order_details.html'
    success_url = reverse_lazy('authority:table_bookig_details', kwargs={'pk': 0})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Confirm Booking"
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.confirmed_at = datetime.now()
            form_obj.save()
        messages.success(self.request, "Order Accepted Successfully")
        self.success_url = reverse_lazy('authority:order_details', kwargs={'pk': self.object.id})
        return super().form_valid(form)
    
class ConfirmDeleveryView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Order
    form_class = ConfirmDeleveryForm
    template_name = 'authority/order_details.html'
    success_url = reverse_lazy('authority:confirmed_order_list')

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


class DeleteOrderView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model= Order
    context_object_name ='order'
    template_name = 'authority/order_details.html'
    success_url = reverse_lazy('authority:confirmed_order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete order Table" 
        context["deleted"] = True
        return context

class ConfirmedOrderListReportView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Order
    queryset = Order.objects.filter(ordered=True, order_confirm=True).order_by('-id')
    filterset_class = OrderFilter
    template_name = 'authority/order_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Confirmed Order List"
        context["orders"] = self.filterset_class(self.request.GET, queryset=self.queryset)
        return context