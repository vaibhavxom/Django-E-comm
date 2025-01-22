from django.db import models
from django.contrib.auth.models import User
from tour_pacage_booking.models import Product


class ShippingAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True ,blank= True)
    Shipping_full_name = models.CharField(max_length=255)
    Shipping_email = models.CharField(max_length=255)
    Shipping_address1 =models.CharField(max_length=255)
    Shipping_address2 =models.CharField(max_length=255)
    Shipping_city =models.CharField(max_length=255)
    Shipping_state =models.CharField(max_length=255, null= True ,blank= True)
    Shipping_zipcode =models.CharField(max_length=255, null= True ,blank= True)
    Shipping_country =models.CharField(max_length=255)

    #dont pluralise address
    class Meta :
        verbose_name_plural = "Shipping Address"

    def __str__(self) :
        return f'Shipping Address = {str(self.id)}'


#order model
class Order(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE,null=True ,blank= True)
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    Shipping_address =models.CharField(max_length=10000)
    amount_pain =models.DecimalField(max_digits=10 , decimal_places= 2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'Order -{str(self.id)}'

#order Item model
class OrderItem(models.Model):
    order = models.ForeignKey(Order ,on_delete=models.CASCADE,null=True )
    product = models.ForeignKey(Product ,on_delete=models.CASCADE,null=True )
    user = models.ForeignKey(User ,on_delete=models.CASCADE,null=True ,blank= True)

    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self) :
        return f'Order Item -{str(self.id)}'




