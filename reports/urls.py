from django.urls import path


app_name = 'report'

# Import Views
from reports.views import OrderListPdfView
from reports.views import StockListPdfView


urlpatterns = [
    path('order_report/', OrderListPdfView.as_view(), name='order_pdf'),
    path('stock_report/', StockListPdfView.as_view(), name='stock_pdf'),
]