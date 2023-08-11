from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Packages for python
import requests
import socket
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal

# Models
from payment.models import BillingAddress
from products.models import Order
from products.models import Cart
from authority.models import ShippingCharge

# Forms
from payment.forms import BillingAddressForm

# Create your views here.
@login_required
def check_out(request):
    saved_address = BillingAddress.objects.get_or_create(user = request.user)[0]
    shipping_charges = ShippingCharge.objects.latest("id")
    form = BillingAddressForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingAddressForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.user = request.user 
            form.save()
            form = BillingAddressForm(instance=saved_address)
    
    order_qs = Order.objects.filter(user=request.user, ordered = False)
    order_items = order_qs[0].orderitems.all()
    total_item = order_qs[0].orderitems.all().count()
    order_total = order_qs[0].get_totals()
    shipping_charge=shipping_charges.shipping_charge
    total_pay = shipping_charge+order_total
           


    return render(request, 'payment/check_out.html', context={'form':form, 'order_items':order_items,'order_total':order_total, 'total_item':total_item, 'saved_address': saved_address,'total_pay':total_pay,'shipping_charge':shipping_charge})


@login_required
def payment(request):

    saved_address = BillingAddress.objects.get_or_create(user = request.user)[0]

    if not saved_address.is_fully_filled():
        messages.info(request, "Please complete your shipping address")
        return redirect('payment:checkout')

    if not request.user.profile.is_fully_filled():
        messages.info(request, "Please complete your profile information.")
        return redirect('home:edit_profile', request.user.id)


    status_url = request.build_absolute_uri(reverse('payment:payment_success'))
    print(status_url)
    shipping_charge = ShippingCharge.objects.latest('id')
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_items_count = order_qs[0].orderitems.count()
    order_total = order_qs[0].get_totals()+shipping_charge.shipping_charge

    current_user = request.user
    full_name = str(current_user.profile.first_name+" "+current_user.profile.last_name)
    print(full_name)

    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id='sizzl64456beb762af', sslc_store_pass='sizzl64456beb762af@ssl')

    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)

    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='food', product_name=order_items, num_of_item=order_items_count, shipping_method='YES', product_profile='None')

    mypayment.set_customer_info(name=full_name, email=current_user.email, address1=current_user.profile.address_1, address2=current_user.profile.address_1, city='Dhaka', postcode='1230', country='Bangladesh', phone=current_user.profile.phone_number)

    mypayment.set_shipping_info(shipping_to=full_name, address=saved_address.address, city=saved_address.city, postcode=saved_address.zip_code, country=saved_address.country)

    response_data = mypayment.init_payment()
    print(response_data)

    return redirect(response_data['GatewayPageURL'])


@csrf_exempt
def complete_payment(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data= request.POST
    
        payment_status = payment_data['status']
        
        if payment_status == 'VALID':
            transaction_id = payment_data['tran_id']
            bank_tran_id = payment_data['bank_tran_id']
            messages.success(request, "Your payment completed Successfully")
            
            return HttpResponseRedirect(reverse('payment:purchase', kwargs={'val_id':bank_tran_id,'tran_id':transaction_id}))
        
        elif payment_status == 'FAILD':
            messages.warning(request, "Your payment Faild, please try again!")
            return HttpResponseRedirect(reverse('payment:checkout'))
        
        else:
            messages.warning(request, "Your payment Faild, please try again!")
            return HttpResponseRedirect(reverse('payment:checkout'))
    
    return render(request, 'payment/payment_success.html', context={})


@login_required
def purchase(request, val_id, tran_id):
    order_qs = Order.objects.filter(user=request.user, ordered=False)[0]
    order_qs.order_id = val_id
    order_qs.payment_id = tran_id
    order_qs.ordered = True
    order_qs.payment_status = True
    order_qs.save()

    cart_items = Cart.objects.filter(user=request.user, purchased=False)
    for item in cart_items:
        item.purchased = True
        item.save()

    return HttpResponseRedirect(reverse('home:my_order'))

@login_required
def cashon_purchase(request):
    order_qs = Order.objects.filter(user=request.user, ordered=False)[0]
    order_qs.ordered = True
    order_qs.save()

    cart_items = Cart.objects.filter(user=request.user, purchased=False)
    for item in cart_items:
        item.purchased = True
        item.save()

