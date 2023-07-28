from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy

#Import Generic Views
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DeleteView

# Models
from products.models import Product

# Permissions Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Form Classes
from products.forms import ProductForm

# Filter Classes
from products.filters import ProductFilter

# Create your views here.
class ProductListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Product
    queryset = Product.objects.filter(is_active= True).order_by('-id')
    template_name = 'products/manage_product.html'
    filterset_class = ProductFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Product List"
        context["products"] = self.filterset_class(self.request.GET, queryset=self.queryset)
        context["list"] = True
        return context
    


class AddProductView(LoginRequiredMixin, AdminPassesTestMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/manage_product.html'
    success_url = reverse_lazy('products:add_subCategory')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Product"
        return context
    

    def form_valid(self, form):
        messages.success(self.request, "Product  Added successfully")
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.error(self.request, "Something wrong try again")
        return super().form_invalid(form)




    
