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

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from deleveryman.permissions import DeleveryManPassesTestMixin

# Import Models
from accounts.models import Profile
from accounts.forms import ProfileForm
from authority.models import ShippingCharge
from products.models import Order




# Create your views here.
class DeleveryManHomeView(LoginRequiredMixin, DeleveryManPassesTestMixin, TemplateView):
    template_name = 'delevery_man/delevery_man.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Customer Panel" 
        context["orders"] = Order.objects.filter(assigned_to=self.request.user, ordered=True, order_confirm=True).order_by('-id')[:10]
        context["pending_order"] = Order.objects.filter(assigned_to=self.request.user, ordered=True, order_confirm=True, delevery_status=False).count()
        context["confirmed_order"] = Order.objects.filter(assigned_to=self.request.user, ordered=True, delevery_status=True).count()
        context["total_orders"] = Order.objects.filter(assigned_to=self.request.user, ordered=True,order_confirm=True ).count()
        return context
