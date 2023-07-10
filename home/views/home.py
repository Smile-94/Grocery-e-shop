from django.shortcuts import redirect


# Generc Classes
from django.views.generic import TemplateView



# Create your views here.
class Home(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home" 
        
        return context