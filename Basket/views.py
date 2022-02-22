from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from Stores.models import Product

from .basket import Basket


def basket_summary(request):
    print(request.session['basket'], request.user)
    basket = Basket(request)
    wish_produits = Product.objects.filter(users_wishlist=request.user)
    print(wish_produits)
    context = {
        'basket': basket,
        'wish_produits': wish_produits
    }
    return render(request, 'summary.html', context)


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        qty = request.POST.get('productqty')
        if qty == '':
            qty = 1
        product_qty = int(qty)
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        print(response)
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        basketsubtotal = basket.get_subtotal_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': basketsubtotal})
        return response

