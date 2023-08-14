from django.urls import path


app_name = 'customer'

#Import Views
from customer.views import CustomerHomeView
from customer.views import MyOrderListView

urlpatterns = [

path('customer/', CustomerHomeView.as_view(), name='customer'),
path('my_pending_order/', MyOrderListView.as_view(), name='my_pending_list')
    
]
