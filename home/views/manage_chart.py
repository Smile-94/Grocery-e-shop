from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum

# Generic Classes
from django.views.generic import TemplateView
from django.views.generic import ListView

# Permission 
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from products.models import Cart
from products.models import Order
from products.models import Product
from accounts.models import User
from authority.models import ShippingCharge


@login_required
def add_to_cart(request, pk):
    # item = get_object_or_404(Product, id=pk)
    item = Product.objects.get(id=pk)
    print("Item", item)

    order_item = Cart.objects.get_or_create(items=item, user=request.user,purchased=False)
    order_qs = Order.objects.filter(user = request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        
        if order.orderitems.filter(items=item).exists():
            order_item[0].quentity +=1
            order_item[0].save()
            return redirect('home:home')
        else:
            order.orderitems.add(order_item[0])
            return redirect('home:home')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        return redirect('home:home')

class ChartProductListView(LoginRequiredMixin, TemplateView):

    template_name = 'home/cart_details.html'

    def get_context_data(self, **kwargs):
        chart_items = Cart.objects.filter(user =self.request.user, purchased = False)
        shipping_charge = ShippingCharge.objects.latest('id')
        total_price = Cart.objects.filter(user=self.request.user, purchased=False).annotate(item_total=F('quentity') * F('items__product_price')).aggregate(total_price=Sum('item_total'))['total_price'] or 0
        discount = 0
        for cart_item in chart_items:
            discount += float(cart_item.get_discount_amount())  # Assuming discount_percentage is defined
        context = super().get_context_data(**kwargs)

        context["title"] = "Cart Page"
        context["products"] = Product.objects.filter(is_active=True).order_by('-id')[:10]
        context["chart_items"] =  chart_items
        context["total_items"] = Cart.objects.filter(user =self.request.user, purchased = False).count()
        context["total_price"] =Cart.objects.filter(user=self.request.user, purchased=False).annotate(item_total=F('quentity') * F('items__product_price')).aggregate(total_price=Sum('item_total'))['total_price'] or 0
        context["shipping_charge"] = shipping_charge
        context["discount"] = discount
        context["shipping_total"] = ((shipping_charge.shipping_charge+total_price)-discount)
        return context

@login_required
def remove_form_cart(request, pk):
    item = get_object_or_404(Product, id = pk)
    order_qs = Order.objects.filter(user = request.user, ordered = False)

    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(items=item).exists():
            order_item = Cart.objects.filter(items=item, user= request.user, purchased=False )[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            return redirect('home:cart_details')
        else:
            return redirect('home:home')
    else:
        return redirect('home:home')

@login_required
def increase_cart_item(request, pk):
    item = get_object_or_404(Product, id = pk)
    order_qs = Order.objects.filter(user = request.user, ordered = False)

    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(items=item).exists():
            order_item = Cart.objects.filter(items=item, user= request.user, purchased=False )[0]

            if order_item.quentity >= 1:
                order_item.quentity +=1
                order_item.save()
            return redirect('home:cart_details')
        else:
            return redirect('home:home')
    else:
        return redirect('home:home')
    
@login_required
def decrease_cart_item(request, pk):
    item = get_object_or_404(Product, id = pk)
    order_qs = Order.objects.filter(user = request.user, ordered = False)

    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(items=item).exists():
            order_item = Cart.objects.filter(items=item, user= request.user, purchased=False )[0]

            if order_item.quentity > 1:
                order_item.quentity -=1
                order_item.save()
                return redirect('home:cart_details')
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                return redirect('home:cart_details')
        else:
            return redirect('home:home')
    else:
        return redirect('home:home')

class MyOrderListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'home/my_order.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user, ordered=True).order_by('id')[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "My order"
        context["shipping_charge"] = ShippingCharge.objects.latest('id')
        return context