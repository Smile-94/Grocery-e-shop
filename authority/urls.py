from django.urls import path

app_name='authority'

# Authority Views
from authority.views import admin_main
from authority.views import manage_order

urlpatterns = [
    path("authority/", admin_main.AdminView.as_view(), name="authority"),
    
]


# Manage Order
urlpatterns += [
    path('pending-order-list/', manage_order.PendingListView.as_view(), name='pending_order_list'),
    path('confirmed-order-list/', manage_order.ConfirmedOrderListView.as_view(), name='confirmed_order_list'),
    path('order-details/<int:pk>/',  manage_order.OrderDetailsView.as_view(), name='order_details'),
    path('order-confirm/<int:pk>/',  manage_order.ConfirmOrderView.as_view(), name='order_confirm'),
    path('order-delete/<int:pk>/',  manage_order.DeleteOrderView.as_view(), name='order_delete'),
    path('order-report/',  manage_order.ConfirmedOrderListReportView.as_view(), name='order_report'),
    path('confirm_delevery/<int:pk>/',  manage_order.ConfirmDeleveryView.as_view(), name='confirm_delevery'),
    
]