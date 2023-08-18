from django.urls import path


app_name = 'deleveryman'

#Import Views
from deleveryman.views import DeleveryManHomeView
from deleveryman.views import DeleveryManPendingListView
from deleveryman.views import DeleveryConfirmedOrderListView
from deleveryman.views import DeleveryConfirmedOrderListView
from deleveryman.views import DeleveryManConfirmDeleveryView
from deleveryman.views import DeleveryManOrderDetailsView

urlpatterns = [

path('deleveryman/', DeleveryManHomeView.as_view(), name='deleveryman'),
path('deleveryman_pending_list/', DeleveryManPendingListView.as_view(), name='deleveryman_pendinglist'),
path('deleveryman_confirmed_list/', DeleveryConfirmedOrderListView.as_view(), name='deleveryman_Confirmed_list'),
path('deleveryman_order_details/<int:pk>/', DeleveryManOrderDetailsView.as_view(), name='deleveryman_order_details'),
path('deleveryman_delevery_confirmed/<int:pk>/', DeleveryManConfirmDeleveryView.as_view(), name='deleveryman_Confirmed'),  
]