from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


# Filters Class
from authority.filters import EmployeeListFilter


# class-based view classes
from django.views.generic import ListView

# Permission and Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin



# Import Models
from accounts.models import User

class CustomerListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = User.objects.filter(is_customer=True)
    filterset_class = EmployeeListFilter
    template_name = 'authority/customer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Deleveryman List"
        context["customers"] = self.filterset_class(self.request.GET, queryset=self.queryset)
        return context