from django.shortcuts import redirect


# Generc Classes
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

# Import Models
from products.models import Product



# Create your views here.
class Home(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home" 
        context["recent_product"] = Product.objects.filter(is_active=True).order_by('-id')[:8] 
        context["featured_product"] = Product.objects.filter(is_active=True, product_type='featured').order_by('-id')[:10] 
        
        return context

class AllProductView(ListView):
    queryset = Product.objects.all()
    template_name = 'home/all_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All Products" 
        context["products"] = self.queryset
        return context

class ProductsDetailsView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'home/products_details.html'

    def get_context_data(self, **kwargs):
        product_pk = self.kwargs['pk']
        product = Product.objects.get(id=product_pk)
        sub_category = product.sub_catagory_1
        context = super().get_context_data(**kwargs)
        context["title"] = "Product Details"
        context["related_products"] = Product.objects.filter(sub_catagory_1=sub_category)[:4]
        return context

    