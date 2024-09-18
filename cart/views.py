from django.shortcuts import render ,get_object_or_404
from .cart import Cart
from tour_pacage_booking.models import Product
from django.http import JsonResponse   
from django.contrib import messages

def cart_summary(request):

    cart = Cart(request)
    cart_products = cart.get_prods
    quantities =cart.get_quants
    totals = cart.cart_total()

    return render(request,"cart_summary.html", {"cart_products":cart_products,"quantities":quantities,"total":totals})



def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity =int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_quantity)
        
        #get cart quantity
        cart_quantity = cart.__len__()

        # Return the response
        #response = JsonResponse({'product_name': product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request,('product added to cart'))
        return response



def cart_delete(request):
     cart =Cart(request)
     if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)
        messages.success(request,('product removed from cart'))
        responce = JsonResponse({'product':product_id})
        
        return responce
        #return redirect('cart_summary')
    



def cart_update(request):
    cart =Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity =int(request.POST.get('product_qty'))

        cart.update(product=product_id,quanitiy=product_quantity)

        responce = JsonResponse({'qty':product_quantity})
        messages.success(request,('product updated'))
        return responce
        #return redirect('cart_summary')

