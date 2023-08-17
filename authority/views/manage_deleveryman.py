from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


# Filters Class
from authority.filters import EmployeeListFilter


# class-based view classes
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Permission and Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Import Signup Form
from accounts.forms import SignUpForm
from accounts.forms import ProfileForm
from deleveryman.forms import DeleveryManInfoForm

# Import Models
from accounts.models import User
from accounts.models import Profile
from deleveryman.models import DeleveryManInfo



class AddDeleveryManView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('authority:deleveryman_list')
    template_name = 'authority/add_deleveryman.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Deleveryman Accounts"
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.is_deleveryman = True
            user.save()
            messages.success(self.request, "Delevery Man Accounts Created Success Fully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "email or password invalid try aging")
        return super().form_invalid(form)


class DeleveryManListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = User.objects.filter(is_deleveryman=True, is_active=True)
    filterset_class = EmployeeListFilter
    template_name = 'authority/delevery_manlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Deleveryman List"
        context["deleverymans"] = self.filterset_class(self.request.GET, queryset=self.queryset)
        return context


class DeleveryManInfoEditView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = User
    model2 = DeleveryManInfo
    form_class = ProfileForm
    form_class2 = DeleveryManInfoForm
    template_name = 'authority/add_delevery_man_info.html'
    success_url = reverse_lazy('authority:add_employee')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user_object = User.objects.get(id=self.kwargs.get('pk'))
            print(user_object)
            context["title"] = "Add/Edit Deleveryman Inof"
            context["form"] = self.form_class(instance=user_object.profile)
            context["form2"] = self.form_class2(instance=user_object.deleveryman_info)
            
        except Exception as e:
            print(e)
        return context
    
    def post(self, request, *args, **kwargs):
        user_object = User.objects.get(id=self.kwargs.get('pk'))
        form = self.form_class(request.POST, request.FILES, instance=user_object.profile)
        form2 = self.form_class2(request.POST, request.FILES, instance=user_object.deleveryman_info)
        return self.form_valid(form, form2)
    
    def form_valid(self, form, form2):
        try:
            if form.is_valid() and form2.is_valid():
                user = form.save(commit=False)
                info = form2.save(commit=False)
                user.profile = User.objects.get(id=self.kwargs.get('pk'))
                info.info_of = User.objects.get(id=self.kwargs.get('pk'))
                user.save()
                info.save()
                messages.success(self.request, "Deleveryman Info Updated Successfully")
            return super().form_valid(form)

        except Exception as e:
            print(e)
            return super().form_invalid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Some thing wrong try again")
        return super().form_invalid(form)