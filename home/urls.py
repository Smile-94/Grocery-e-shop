from django.urls import path

app_name='home'

# Home Views
from home.views import home

urlpatterns = [
    path("", home.Home.as_view(), name="home"),
    path("all-product", home.AllProductView.as_view(), name="all_products"),
    path("product-details/<int:pk>/", home.ProductsDetailsView.as_view(), name="product_details"),
    
]