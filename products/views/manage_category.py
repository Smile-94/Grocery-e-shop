from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages
from django.shortcuts import redirect


# Django Generic View
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Permission
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Import Models
from products.models import Category

# Forms
from products.forms import CategoryForm

# Filters
from products.filters import CategoryFilters


# Class-based View for add and List Dsiplay of Category
class AddCategoryView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):

    model = Category
    form_class = CategoryForm
    queryset = Category.objects.filter(is_active= True).order_by('-id')
    template_name = 'products/manage_category.html'
    success_url = reverse_lazy('products:add_category')
    filterset_class = CategoryFilters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Category"
        context["categories"] = self.filterset_class(self.request.GET, queryset=self.queryset)
        return context
    

    def form_valid(self, form):
        messages.success(self.request, "Product Category Added successfully")
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.error(self.request, "Something wrong try again")
        return super().form_invalid(form)




class UpdateProductsCategoryView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):

    model = Category
    form_class = CategoryForm
    queryset = Category.objects.filter(is_active= True).order_by('-id')
    template_name = 'products/manage_category.html'
    success_url = reverse_lazy('products:add_category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Category"
        context["updated"] = True
        return context
    

    def form_valid(self, form):
        messages.success(self.request, "Product Category Updated successfully")
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, try again!")
        return super().form_invalid(form)
    

class DeleteCategoryView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model= Category
    template_name = 'products/manage_category.html'
    success_url = reverse_lazy('products:add_category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Category" 
        context["deleted"] = True
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        messages.success(self.request, "Product Category Deleted Successfully")
        return redirect(self.success_url)
    
    def form_invalid(self, form):
        messages.error(self.request, "Someting went worng, try again!")
        return super().form_invalid(form)

    
