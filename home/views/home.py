from django.shortcuts import redirect


# Generc Classes
from django.views.generic import TemplateView

# Import Models
from products.models import Product



# Create your views here.
class Home(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home" 
        context["recent_product"] = Product.objects.filter(is_active=True).order_by('-id')[:10] 
        
        return context