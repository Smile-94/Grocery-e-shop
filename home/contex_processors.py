from products.models import Cart
from django.db.models import F, Sum


def my_context_processor(request):
    data_dic = {}
    try:

        chart_items = Cart.objects.filter(user = request.user, purchased = False)
        chart_item_quetity = Cart.objects.filter(user = request.user, purchased = False).count()
        data_dic.update({
            'chart_items':chart_items,
            'chart_item_quetity':chart_item_quetity,
        })
    except Exception as e:
        print(e)
    
    return data_dic