from django.urls import path

app_name='authority'

# Authority Views
from authority.views import admin_main
from authority.views import manage_order
from authority.views import manage_deleveryman
from authority.views import manage_customer
from authority.views import reports

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

# Manage Delevery Man
urlpatterns += [
    path('add-deleveryman/',  manage_deleveryman.AddDeleveryManView.as_view(), name='add_deleveryman'),
    path('deleveryman-list/', manage_deleveryman.DeleveryManListView.as_view(), name='deleveryman_list'),
    path('edit-delevery-man-info/<int:pk>/', manage_deleveryman.DeleveryManInfoEditView.as_view(), name='edit_deleveryman_info'),  
]

# Manage Customer
urlpatterns += [
    
    path('customer-list/', manage_customer.CustomerListView.as_view(), name='customer_list'),
    
]

# Manage Customer
urlpatterns += [
    
    path('orders-report/', reports.ReportOrderView.as_view(), name='order_report'),
    path('stock-report/', reports.StockReportView.as_view(), name='stock_report'),
    
]