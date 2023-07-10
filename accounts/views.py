from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


# Permission and Authentication
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib.auth.mixins import LoginRequiredMixin


# class based view builtin class
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic import CreateView

# Models
from accounts.models import User

# forms
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import SignUpForm


# Create your views here.
class SignupView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Customer Signup"
        return context
    
    def form_valid(self, form):
        try:
            form_obj=form.save()
            form_obj.is_customer = True
            form_obj.save()
            messages.success(self.request, "Welcome to Sizzling Station")
            return super().form_valid(form)
        
        except Exception as e:
            print(e)
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        email = form.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(self.request, "Thsi email already exist try another or login")
        return super().form_invalid(form)
        
    


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home:home')
    template_name = 'accounts/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login Page" 
        return context
    
    
    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password']

        try:
            request_user = User.objects.get(email=username)
            user = authenticate(self.request, username=username, password=password)

            if user is not None and request_user.is_superuser is True and request_user.is_staff is True:
                login(self.request, user)
                return HttpResponseRedirect(reverse('authority:authority'))
            
            elif user is not None and request_user.is_customer is True:
                login(self.request, user)
                self.success_url = self.request.GET.get('next', self.success_url)
                return HttpResponseRedirect(self.get_success_url())

            elif user is not None and request_user.is_deleveryman is True:
                login(self.request, user)
                return HttpResponse("Delevery Man login page will implement soon")

            
            else:
                if User.objects.filter(email=username).exists() and request_user.is_active is False:
                    messages.warning(self.request, f"{username} this email don't have login permission")
                
                return HttpResponseRedirect(reverse('accounts:login'))

        except Exception as e:
            print(e)
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid User email password")
        return super().form_invalid(form)
    

class UserLogout(LoginRequiredMixin, LogoutView):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        logout(request)
        if user.is_customer:
           return redirect(reverse('home:home'))
        return redirect(reverse('accounts:login'))