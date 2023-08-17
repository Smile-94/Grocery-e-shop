from django.shortcuts import redirect
from datetime import datetime,timedelta
from datetime import date

from django.db.models import Count, Sum
from django.utils import timezone

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Generc Classes
from django.views.generic import TemplateView

# Import Models
from products.models import Order



# Create your views here.
class AdminView(LoginRequiredMixin, AdminPassesTestMixin, TemplateView):
    template_name = 'authority/admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Admin Panel" 
        context["orders"] = Order.objects.filter(ordered=True, order_confirm=False, delevery_status=False ).order_by('-id')[:10]
        context["total_order"] = Order.objects.filter(ordered=True).count()
        context["pending_order"] = Order.objects.filter(ordered=True, order_confirm=False, delevery_status=False ).count()
        context["confirm_order"] = Order.objects.filter(ordered=True, order_confirm=True).count()
        context["delevered_order"] = Order.objects.filter(ordered=True, order_confirm=True, delevery_status=True ).count()
        return context