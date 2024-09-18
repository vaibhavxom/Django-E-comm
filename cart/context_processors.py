from .cart import Cart

#context processor to work all the pages
def cart(request):
    return {'cart': Cart(request)}