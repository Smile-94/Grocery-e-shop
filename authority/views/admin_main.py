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



# Create your views here.
class AdminView(LoginRequiredMixin, AdminPassesTestMixin, TemplateView):
    template_name = 'authority/admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Admin Panel" 
        
        return context