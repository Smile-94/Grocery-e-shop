from django.urls import path

app_name='home'

# Home Views
from home.views import home
from home.views import manage_chart

urlpatterns = [
    path("", home.Home.as_view(), name="home"),
    path("home/", home.Home.as_view(), name="home"),
    path("all-product", home.AllProductView.as_view(), name="all_products"),
    path("product-details/<int:pk>/", home.ProductsDetailsView.as_view(), name="product_details"),
    
]


# manage order
urlpatterns += [
    path('add-to-cart/<int:pk>/', manage_chart.add_to_cart, name='add_to_cart'),
    path('cart-details/', manage_chart.ChartProductListView.as_view(), name='cart_details'),
    path('remove-from_cart/<int:pk>/', manage_chart.remove_form_cart, name='remove_form_cart'),
    path('increase-from-cart/<int:pk>/',manage_chart.increase_cart_item, name='increase_cart'),
    path('decrease-from-cart/<int:pk>/',manage_chart.decrease_cart_item, name='decrease_cart'),
    path('my-order/', manage_chart.MyOrderListView.as_view(),name="my_order"),
]