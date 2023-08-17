from django.urls import path


app_name = 'customer'

#Import Views
from customer.views import CustomerHomeView
from customer.views import MyOrderListView
from customer.views import MyConfirmedOrderListView
from customer.views import AddProfileInfo

urlpatterns = [

path('customer/', CustomerHomeView.as_view(), name='customer'),
path('my_pending_order/', MyOrderListView.as_view(), name='my_pending_list'),
path('my_confirmed_order/', MyConfirmedOrderListView.as_view(), name='my_confirmed_list'),
path('edit-profile/<int:pk>/', AddProfileInfo.as_view(),name="edit_profile")
    
]
