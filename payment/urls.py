from django.urls import path

app_name = 'payment'

from payment.views import check_out
from payment.views import payment
from payment.views import complete_payment
from payment.views import purchase
from payment.views import cashon_purchase

urlpatterns = [
    path('checkout/', check_out, name='checkout'),
    path('payment/', payment, name='payment'),
    path('payment-success/', complete_payment, name='payment_success'),
    path('purchase/<val_id>/<tran_id>/', purchase, name='purchase'),
    path('cash-on-purchase/', cashon_purchase, name='cash_on_purchase'),
]