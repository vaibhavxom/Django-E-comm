from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages
from cart.cart import Cart

def checkout(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        return render(request, "payment/checkout.html", {
            "cart_products": cart_products,
            "quantities": quantities,
            "total": totals
        })
    else:
        # Add a message before redirecting to the login page
        messages.info(request, "You need to log in to proceed to checkout.")
        return redirect('login')  # Replace 'login' with the name of your login URL pattern

def payment_success(request):
    return render(request, "payment/payment_success.html", {})