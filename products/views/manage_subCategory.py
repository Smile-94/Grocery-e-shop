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
from products.models import SubCategory

# Forms
from products.forms import SubCategoryForm

# Filters
from products.filters import SubCategoryFilters


# Class-based View for add and List Dsiplay of Category
class AddSubCategoryView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):

    model = SubCategory
    form_class = SubCategoryForm
    queryset = SubCategory.objects.filter(is_active= True).order_by('-id')
    template_name = 'products/manage_sub_category.html'
    success_url = reverse_lazy('products:add_subCategory')
    filterset_class = SubCategoryFilters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Sub-Category"
        context["subcategories"] = self.filterset_class(self.request.GET, queryset=self.queryset)
        return context
    

    def form_valid(self, form):
        messages.success(self.request, "Product Sub-Category Added successfully")
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.error(self.request, "Something wrong try again")
        return super().form_invalid(form)




class UpdateProductsSubCategoryView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):

    model = SubCategory
    form_class = SubCategoryForm
    queryset = SubCategory.objects.filter(is_active= True).order_by('-id')
    template_name = 'products/manage_sub_category.html'
    success_url = reverse_lazy('products:add_subCategory')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Sub-Category"
        context["updated"] = True
        return context
    

    def form_valid(self, form):
        messages.success(self.request, "Product Sub-Category Updated successfully")
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, try again!")
        return super().form_invalid(form)
    

class DeleteSubCategoryView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model= SubCategory
    template_name = 'products/manage_sub_category.html'
    success_url = reverse_lazy('products:add_subCategory')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Sub-Category" 
        context["deleted"] = True
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        messages.success(self.request, "Product Sub-Category Deleted Successfully")
        return redirect(self.success_url)
    
    def form_invalid(self, form):
        messages.error(self.request, "Someting went worng, try again!")
        return super().form_invalid(form)