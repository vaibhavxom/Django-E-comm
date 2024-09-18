from tour_pacage_booking.models import Product,Profile


class Cart():
    def __init__(self,request):
        self.session = request.session
        #get requset    
        self.request = request
        #get the current session key if exist
        cart = self.session.get('session_key')

        #if the user is new , no session key! create new session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # make sure cart is availabe to all pages
        self.cart = cart
    def db_add(self,product,quantity):
        product_id = str(product) 
        product_qty =str(quantity)

        #logic 
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True 
        # to deal with login user 
        if self.request.user.is_authenticated :
            #get current user 
            current_user = Profile.objects.filter(user__id = self.request.user.id) 
            #covert python dicsonary back to string 
            carty = str(self.cart)
            carty = carty.replace("\'","\"")

            current_user.update(old_cart = str(carty))


    def add(self,product,quantity):
        product_id = str(product.id) 
        product_qty =str(quantity)

        #logic 
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True 
        # to deal with login user 
        if self.request.user.is_authenticated :
            #get current user 
            current_user = Profile.objects.filter(user__id = self.request.user.id) 
            #covert python dicsonary back to string 
            carty = str(self.cart)
            carty = carty.replace("\'","\"")

            current_user.update(old_cart = str(carty))

#new logic corrected by chatGpt
    def cart_total(self):
    # Get product ids
        product_ids = list(map(int, self.cart.keys()))
        
        # Lookup keys in db models
        products = Product.objects.filter(id__in=product_ids)
        
        # Create a dictionary to map product ids to product objects
        product_dict = {product.id: product for product in products}
        
        # Calculate total
        total = 0
        for product_id, quantity in self.cart.items():
            product_id = int(product_id)  # Ensure id is an integer
            product = product_dict.get(product_id)
            if product:
                if product.is_sale:
                    total += product.sale_price * quantity
                else:
                    total += product.price * quantity
        
        return total


#old logic for total
    # def cart_total(self):
    #     #get product ids
    #     product_ids =self.cart.keys()
    #     #looksup keys in db models
    #     products = Product.objects.filter(id__in=product_ids)
    #     #get quantity
    #     quantities = self.cart
    #     total = 0
    #     for key, value in quantities.items():
    #         #convert key sting into int  
    #         key = int(key)
    #         for product in products:
    #             if product.id ==key:
    #                 if product.is_sale:
    #                     total =total +(product.sale_price * value)
    #             else:
    #                 total =total +(product.price * value)
    #     return total



    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #get ids from cart
        product_ids = self.cart.keys()
        #use ids to lookup product in db model
        products = Product.objects.filter(id__in=product_ids)
        #return products 
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities
    

    def update(self,product,quanitiy):
        product_id =str(product)
        product_qty =int(quanitiy)
        
        #get cart

        ourcart = self.cart 
        #update cart 
        ourcart[product_id] = product_qty
        

        self.session.modified = True
        # to deal with login user 
        if self.request.user.is_authenticated :
            #get current user 
            current_user = Profile.objects.filter(user__id = self.request.user.id) 
            #covert python dicsonary back to string 
            carty = str(self.cart)
            carty = carty.replace("\'","\"")

            current_user.update(old_cart = str(carty))
        thing = self.cart

        return thing 
    
    def delete(self,product):
        product_id =str(product)
        #delete from cart 
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified=True

        # to deal with login user 
        if self.request.user.is_authenticated :
            #get current user 
            current_user = Profile.objects.filter(user__id = self.request.user.id) 
            #covert python dicsonary back to string 
            carty = str(self.cart)
            carty = carty.replace("\'","\"")

            current_user.update(old_cart = str(carty))

